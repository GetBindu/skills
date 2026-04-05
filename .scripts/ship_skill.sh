#!/usr/bin/env bash
# ship_skill.sh — lint, commit, push, and announce a single skill.
#
# Usage:
#   ./.scripts/ship_skill.sh <skill-name> [commit-message]
#   ./.scripts/ship_skill.sh zinc-database
#   ./.scripts/ship_skill.sh zinc-database "fix broken URL syntax"
#   ./.scripts/ship_skill.sh --dry-run zinc-database        # don't push
#   ./.scripts/ship_skill.sh --no-push zinc-database        # commit only
#   ./.scripts/ship_skill.sh --no-slack zinc-database       # skip Slack post
#
# Steps:
#   1. Run ruff check --fix on the skill's scripts/
#   2. Run ruff format on the skill's scripts/
#   3. git add <skill>/
#   4. git commit with message
#   5. git push (unless --no-push or --dry-run)
#   6. Post ship notification to #skills on Slack
#
# Slack posts happen through Claude Code's /skills ping flow — this script
# just produces the data that Claude then posts. The notification should
# include:
#   - commit SHA + GitHub link
#   - what the skill does
#   - env vars required (auto-detected from scripts and SKILL.md)
#   - dependencies
#   - test command

set -e

SKILLS_ROOT="/Users/raahuldutta/Documents/GetBindu/skills"
DRY_RUN=false
NO_PUSH=false
NO_SLACK=false

# Parse flags
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=true; shift ;;
        --no-push) NO_PUSH=true; shift ;;
        --no-slack) NO_SLACK=true; shift ;;
        --help|-h)
            head -25 "$0" | tail -22
            exit 0
            ;;
        *) break ;;
    esac
done

SKILL="$1"
MESSAGE="${2:-}"

if [[ -z "$SKILL" ]]; then
    echo "Usage: $0 [--dry-run|--no-push|--no-slack] <skill-name> [commit-message]"
    exit 1
fi

SKILL_DIR="$SKILLS_ROOT/$SKILL"
if [[ ! -d "$SKILL_DIR" ]]; then
    echo "Error: skill not found: $SKILL_DIR"
    exit 1
fi

cd "$SKILLS_ROOT"

echo "════════════════════════════════════════════════════════"
echo " Shipping: $SKILL"
echo "════════════════════════════════════════════════════════"

# ─── 1. Lint ───
if [[ -d "$SKILL_DIR/scripts" ]]; then
    echo ""
    echo "[1/6] ruff check --fix..."
    ruff check "$SKILL/scripts" --fix 2>&1 | tail -5 || true

    echo "[2/6] ruff format..."
    ruff format "$SKILL/scripts" 2>&1 | tail -3 || true

    echo "[3/6] ruff check (final)..."
    if ! ruff check "$SKILL/scripts" 2>&1; then
        echo ""
        echo "⚠️  Ruff found issues. Review above before pushing."
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        [[ ! $REPLY =~ ^[Yy]$ ]] && exit 1
    fi
fi

# ─── 2. Show what's staged ───
echo ""
echo "[4/6] Changes to commit:"
git add "$SKILL/"
git status --short "$SKILL/" | head -30

# Check if there's anything to commit
if git diff --cached --quiet "$SKILL/"; then
    echo ""
    echo "✓ No changes in $SKILL/ — nothing to commit."
    exit 0
fi

# ─── 3. Commit ───
if [[ -z "$MESSAGE" ]]; then
    MESSAGE="chore($SKILL): lint and tidy"
fi

echo ""
echo "[5/6] Commit message: $MESSAGE"

if $DRY_RUN; then
    echo ""
    echo "── DRY RUN — not committing ──"
    git reset HEAD "$SKILL/" > /dev/null
    exit 0
fi

git commit -m "$MESSAGE

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

COMMIT_SHA=$(git rev-parse --short HEAD)

# ─── 4. Push ───
if $NO_PUSH; then
    echo ""
    echo "✓ Committed $COMMIT_SHA (not pushed, --no-push flag)."
else
    echo ""
    echo "[6/6] Pushing to origin..."
    git push
    echo "✓ Pushed $COMMIT_SHA."
fi

echo ""
echo "════════════════════════════════════════════════════════"
echo " ✓ Done: $SKILL ($COMMIT_SHA)"
echo "════════════════════════════════════════════════════════"

# ─── 5. Emit ship metadata for Claude to read and post to Slack ───
# Use Python to detect env vars and deps (avoids shell quoting hell)
SHIP_META=$(python3 - "$SKILL_DIR" <<'PYEOF'
import os, re, sys
from pathlib import Path

skill_dir = Path(sys.argv[1])
scripts_dir = skill_dir / "scripts"

env_vars = set()
deps = set()

STDLIB = {
    "argparse", "json", "os", "sys", "re", "pathlib", "subprocess", "shutil",
    "tempfile", "base64", "time", "datetime", "typing", "collections", "itertools",
    "functools", "math", "random", "io", "urllib", "hashlib", "logging", "copy",
    "glob", "csv", "xml", "html", "email", "mimetypes", "gzip", "zipfile",
    "tarfile", "sqlite3", "pickle", "dataclasses", "enum", "abc", "string",
    "operator", "warnings", "ast", "textwrap", "contextlib", "dataclass", "uuid",
}

if scripts_dir.is_dir():
    for py in scripts_dir.rglob("*.py"):
        try:
            src = py.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in re.finditer(r'os\.environ(?:\.get)?\(["\']([A-Z][A-Z0-9_]*)["\']', src):
            env_vars.add(m.group(1))
        for m in re.finditer(r'^\s*(?:from|import)\s+([a-z][a-z0-9_]*)', src, re.MULTILINE):
            name = m.group(1)
            if name not in STDLIB:
                deps.add(name)

print(f"ENV_VARS={','.join(sorted(env_vars)) or 'none'}")
print(f"DEPS={','.join(sorted(deps)) or 'stdlib only'}")
PYEOF
)
ENV_VARS=$(echo "$SHIP_META" | awk -F= '/^ENV_VARS=/{print $2}')
DEPS=$(echo "$SHIP_META" | awk -F= '/^DEPS=/{print $2}')

# Output metadata for Claude to use
cat <<EOF

═══ Ship metadata for Slack post ═══
SKILL: $SKILL
COMMIT: $COMMIT_SHA
COMMIT_URL: https://github.com/GetBindu/skills/commit/$COMMIT_SHA
MESSAGE: $MESSAGE
ENV_VARS: ${ENV_VARS:-none}
DEPENDENCIES: ${DEPS:-stdlib only}
═══════════════════════════════════

EOF

if ! $NO_SLACK && ! $NO_PUSH; then
    echo "→ Next: Post to Slack #skills with the metadata above."
    echo "  (Claude handles this via the slack_send_message tool)"
fi
