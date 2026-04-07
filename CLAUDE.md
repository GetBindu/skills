# GetBindu Skills Repository

Scientific skills for Agno and Claude agents. ~340 skills covering bioinformatics, chemistry, data science, government data, research tools, and more.

## Active work: Skill shipping SOP

We are shipping skills one at a time using a 9-step SOP. Each skill gets: inspected → fixed → smoke tested → Agno agent tested → README written → committed/pushed → Slack notified → API pushed (auto via GA).

**To resume**: Read `.claude/RESUME.md` for full context — shipped log, pending queue, credentials, templates, and patterns.

**Quick command**: `cat .claude/RESUME.md | head -50` to see current state.

## Key files

| File | Purpose |
|------|---------|
| `.claude/RESUME.md` | Session resume guide (shipped log, pending queue, templates) |
| `.scripts/SHIP_PROCESS.md` | Canonical 8-step SOP documentation |
| `.scripts/ship_skill.sh` | Per-skill lint + commit + push script |
| `.gitignore` | Ignores `__pycache__/`, `.venv/`, `.DS_Store`, `.claude/`, `*/upstream/` |
| `pyproject.toml` | Ruff lint + format config (target Python 3.9) |

## Rules

- **One skill at a time.** Don't batch-fix many skills.
- **Test before push.** Smoke test (Step 4) and Agno test (Step 5) must pass before shipping (Step 7).
- **Every shipped skill needs a README.md** with inputs, outputs, env vars, dependencies, and Agno verdict.
- **Slack post is the last step.** Post to `#skills` (C0AQHL7KNTH) after push.
- **Don't commit** `.venv/`, `__pycache__/`, or stray CLI artifacts.

## Agno compatibility requirements

Skills must use only these YAML frontmatter keys: `name`, `description`, `license`, `metadata`, `compatibility`, `allowed-tools`. Any other keys (like `source`, `source_type`, `repository_url`) must go under `metadata:`.

- Directory name must match `name:` field exactly
- Only hyphens allowed in names (no underscores)
- `metadata:` value must be a dict, not a string

## Tooling

```bash
export PATH="$HOME/.local/bin:$PATH"  # for uv + ruff
ruff check .          # lint
ruff check . --fix    # auto-fix
ruff format .         # format
```

## Agno single-skill tester

```bash
cd /tmp/agno-test && source .venv/bin/activate
export OPENROUTER_API_KEY=sk-or-v1-...
python3 test_skill_one.py <skill-name>
python3 test_skill_one.py <skill-name> --dry-run  # just load, no LLM
```
