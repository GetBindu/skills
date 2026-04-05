#!/usr/bin/env bash
# ship_skill.sh — lint, commit, and push a single skill.
#
# Usage:
#   ./.scripts/ship_skill.sh <skill-name> [commit-message]
#   ./.scripts/ship_skill.sh zinc-database
#   ./.scripts/ship_skill.sh zinc-database "fix broken URL syntax"
#   ./.scripts/ship_skill.sh --dry-run zinc-database        # don't push
#   ./.scripts/ship_skill.sh --no-push zinc-database        # commit only
#
# Steps:
#   1. Run ruff check --fix on the skill's scripts/
#   2. Run ruff format on the skill's scripts/
#   3. git add <skill>/
#   4. git commit with message
#   5. git push (unless --no-push or --dry-run)

set -e

SKILLS_ROOT="/Users/raahuldutta/Documents/GetBindu/skills"
DRY_RUN=false
NO_PUSH=false

# Parse flags
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=true; shift ;;
        --no-push) NO_PUSH=true; shift ;;
        --help|-h)
            head -18 "$0" | tail -15
            exit 0
            ;;
        *) break ;;
    esac
done

SKILL="$1"
MESSAGE="${2:-}"

if [[ -z "$SKILL" ]]; then
    echo "Usage: $0 [--dry-run|--no-push] <skill-name> [commit-message]"
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
    echo "[1/5] ruff check --fix..."
    ruff check "$SKILL/scripts" --fix 2>&1 | tail -5 || true

    echo "[2/5] ruff format..."
    ruff format "$SKILL/scripts" 2>&1 | tail -3 || true

    echo "[3/5] ruff check (final)..."
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
echo "[4/5] Changes to commit:"
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
echo "[5/5] Commit message: $MESSAGE"

if $DRY_RUN; then
    echo ""
    echo "── DRY RUN — not committing ──"
    echo "Would run:"
    echo "  git commit -m \"$MESSAGE\""
    $NO_PUSH || echo "  git push"
    # Unstage so user isn't left with stuff staged
    git reset HEAD "$SKILL/" > /dev/null
    exit 0
fi

git commit -m "$MESSAGE

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# ─── 4. Push ───
if $NO_PUSH; then
    echo ""
    echo "✓ Committed (not pushed, --no-push flag)."
else
    echo ""
    echo "Pushing to origin..."
    git push
    echo "✓ Pushed."
fi

echo ""
echo "════════════════════════════════════════════════════════"
echo " ✓ Done: $SKILL"
echo "════════════════════════════════════════════════════════"
