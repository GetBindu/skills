# Skill Ship Process (SOP)

**Goal:** Ship one skill at a time, end-to-end, in a predictable order. One commit per skill. One Slack post per skill. **Test before push. Ship only when confident.**

---

## The 8 Steps

For **each** skill, execute these steps in order. Don't skip ahead, don't batch.

```
1. Select  →  2. Inspect  →  3. Fix  →  4. Smoke test  →  5. Agno test  →  6. README  →  7. Ship  →  8. Slack
                                         ↑ must pass        ↑ must pass                ↑ only if 4+5 pass
```

### Step 1 — Select the next skill

```bash
# Pick the next one alphabetically, reverse order (end → start, per user preference)
ls -d /Users/raahuldutta/Documents/GetBindu/skills/*/ | awk -F/ '{print $(NF-1)}' | sort -r
```

Skip skills already shipped (see Shipped Log at bottom).

### Step 2 — Inspect the skill

```bash
SKILL=<name>
cd /Users/raahuldutta/Documents/GetBindu/skills/$SKILL
cat SKILL.md | head -40
ls -la scripts/ references/ 2>/dev/null
```

Check:
- Valid YAML frontmatter starting with `---`?
- `name:` matches directory name? (Agno requires hyphens, no underscores)
- Only Agno-allowed keys: `name`, `description`, `license`, `metadata`, `compatibility`, `allowed-tools`?
- Scripts exist and import real libraries (not placeholder stubs)?
- README.md exists with inputs/outputs?

### Step 3 — Fix issues in-place

Only touch **this one skill's files**. Do not fix other skills.

Common fixes:
- **Non-Agno frontmatter keys** (`source`, `source_type`, `repository_url`): move under `metadata:`
- **Stub scripts**: replace with a real working demo
- **Missing venv instructions in SKILL.md**: add the one-liner
- **Broken URLs / deprecated APIs**: rewrite to use a working alternative
- **Directory rename** (underscore → hyphen): `git mv` + update `name:` field

### Step 4 — Smoke test (direct script run)

Must pass before proceeding.

```bash
cd /Users/raahuldutta/Documents/GetBindu/skills/$SKILL
python3 -m venv .venv && source .venv/bin/activate && pip install <deps> -q
python3 scripts/<main>.py <basic-args>
```

Capture:
- The exact command used (input)
- The output produced (first 20 lines is enough)
- Any env vars the script needed
- The pip dependencies installed

If the script errors → go back to Step 3.

### Step 5 — Agno agent test

Must pass before proceeding.

```bash
cd /tmp/agno-test && source .venv/bin/activate
OPENROUTER_API_KEY=sk-or-v1-... python3 test_skill_one.py $SKILL
```

Uses a tester that **loads only this one skill** (via symlink in a temp dir) so unrelated broken skills don't block loading. The agent is asked to invoke the skill with a basic example and print the result.

Capture the Agno response — it goes in the Slack post and README.

If Agno errors on this specific skill → go back to Step 3.
If Agno errors because of this skill + loading strategy bug → fix the tester, not other skills.

### Step 6 — Write / update the skill's `README.md`

Every shipped skill must have a `README.md` with this structure:

```markdown
# <skill-name>

<one-sentence description>

## What it does

<2-3 sentences explaining the behavior>

## Setup

```bash
cd <skill-dir>
python3 -m venv .venv && source .venv/bin/activate && pip install <deps> -q
```

## Environment variables

| Name | Required | Description |
|------|----------|-------------|
| FOO_API_KEY | yes | ... |

(Or "None — uses free public API" if no keys needed.)

## Usage

### Input
```bash
python3 scripts/<main>.py --<flag> "<example value>"
```

### Output
```json
{ ... }
```

(Show the actual output from the smoke test.)

## Dependencies

- `package1`
- `package2`

## Tested with

- Direct script run: ✅
- Agno agent (Claude Haiku via OpenRouter): ✅

<Agno response excerpt>
```

### Step 7 — Ship (lint + commit + push)

**Only when Steps 4 and 5 both passed.** Ship never happens on a skill that hasn't been tested.

```bash
cd /Users/raahuldutta/Documents/GetBindu/skills
./.scripts/ship_skill.sh $SKILL "fix($SKILL): <one-line summary>

- bullet 1
- bullet 2
- bullet 3"
```

### Step 8 — Post to Slack `#skills` (C0AQHL7KNTH)

Last step. Must include all of:
- Commit SHA + GitHub link
- What the skill does
- Env vars required (explicit — name each one, or say "None")
- Dependencies
- **Input example** (actual command run in Step 4)
- **Output example** (actual output captured in Step 4)
- Agno agent response excerpt (from Step 5)

Template:

```
✅ *<skill-name>* shipped

*Commit:* `<sha>` — https://github.com/GetBindu/skills/commit/<sha>

*What it does*
<1-2 sentences>

*Env vars required*
<list or "None">

*Dependencies*
<deps>

*Input*
```
python3 scripts/<main>.py --<flag> "<value>"
```

*Output*
```
<first 10-15 lines of actual output from Step 4>
```

*Agno agent verdict*
<2-3 line excerpt from Step 5 showing the agent successfully used the skill>

*README:* <skill-name>/README.md
```

---

## Hard rules

- ❌ **No push before Agno test passes.** If Agno can't test it, don't ship it.
- ❌ No batch fixes across many skills
- ❌ No reverting other skills' fixes to satisfy Agno loading
- ❌ No committing `.venv/`, `__pycache__/`, or stray CLI artifacts (`Search`, `Use` files)
- ❌ No skipping the Slack post
- ❌ No skipping the README
- ❌ No mid-flight rebases with dirty working tree

---

## Shipped Log

| # | Skill | Commit | Agno tested | README | Slack |
|---|-------|--------|-------------|--------|-------|
| 1 | zinc-database | `beb7077` | ⚠️ direct only | ❌ | ✅ |
| 2 | zarr-python | `f6a64ca` | ⚠️ direct only | ❌ | ✅ |
| 3 | youtu-agent | `351bf95` | ⚠️ direct only | ❌ | ❌ |

**Backfill:** the first 3 shipped under the old SOP (test-after-push). They need READMEs added and Agno re-verification. Do these before starting the next skill.
