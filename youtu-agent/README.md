# youtu-agent

Bootstrapper for the TencentCloudADP/youtu-agent framework — clones the upstream repo, installs its dependencies, and runs the agent CLI.

## What it does

This skill is a **bootstrapper**, not a bundled copy of the framework. It provides three modes:

1. `--info` — reports environment status (Python version, git/uv availability, whether the upstream repo is cloned, whether LLM API keys are set)
2. `--setup` — clones `https://github.com/TencentCloudADP/youtu-agent` into `upstream/youtu-agent/` and runs `uv sync`
3. `--config <name>` — delegates to upstream `scripts/cli_chat.py` with the given agent config (e.g., `simple/base`, `simple/base_search`)

The actual framework and configs live in the upstream repo. This skill just makes it reproducible to bring it up on any machine.

## Setup

No setup required for `--info`. For `--setup` and `--config` modes:

```bash
# Install uv if missing
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repo + install upstream deps
cd youtu-agent
python3 scripts/youtu_agent_client.py --setup
```

## Environment variables

| Name | Required | Description |
|------|----------|-------------|
| `UTU_LLM_API_KEY` | Yes (for `--config`) | LLM provider API key (DeepSeek, OpenAI, or any OpenAI-compatible endpoint) |
| `UTU_LLM_MODEL` | Yes (for `--config`) | Model name, e.g. `deepseek-chat`, `gpt-4o` |
| `UTU_LLM_BASE_URL` | Yes (for `--config`) | Provider base URL, e.g. `https://api.deepseek.com/v1` |
| `SERPER_API_KEY` | Optional | For web search tool |
| `JINA_API_KEY` | Optional | For web reading tool |

None are required for `--info` (which just reports what's set).

## Usage

### Input — environment check
```bash
python3 scripts/youtu_agent_client.py --info
```

### Output
```json
{
  "skill": "youtu_agent",
  "repository": "https://github.com/TencentCloudADP/youtu-agent.git",
  "paper": "https://arxiv.org/abs/2512.24615",
  "environment": {
    "python": "3.9.6",
    "git": true,
    "uv": false,
    "upstream_cloned": false,
    "upstream_venv": false,
    "env_vars": {
      "UTU_LLM_API_KEY": false,
      "UTU_LLM_MODEL": "not set",
      "UTU_LLM_BASE_URL": "not set",
      "SERPER_API_KEY": false,
      "JINA_API_KEY": false
    }
  },
  "next_steps": [
    "Run: python youtu_agent_client.py --setup"
  ]
}
```

### Other input modes
```bash
# Clone + install upstream deps (one-time)
python3 scripts/youtu_agent_client.py --setup

# Run an agent config (after --setup and env vars set)
UTU_LLM_API_KEY=sk-... UTU_LLM_MODEL=deepseek-chat UTU_LLM_BASE_URL=https://api.deepseek.com/v1 \
  python3 scripts/youtu_agent_client.py --config simple/base

# With web search tools
python3 scripts/youtu_agent_client.py --config simple/base_search
```

## CLI flags

| Flag | Description |
|------|-------------|
| `--info` | Report environment + env var status (no side effects) |
| `--setup` | Clone upstream repo + run `uv sync` |
| `--config <name>` | Run upstream `cli_chat.py` with the given YAML config |
| `--format {json,summary}` | Output format for status reports |

## Dependencies

- **Script itself:** Python stdlib only
- **For `--setup`:** `git`, `uv`
- **For `--config`:** everything above + an LLM API key + the upstream repo's dependencies (managed by `uv sync`)

## Tested with

- **Direct script run (`--info`):** ✅ Reports clean env status with accurate missing-tool detection
- **`--help`:** ✅ Argparse help renders correctly
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran `--info`, parsed the JSON output, correctly identified Python 3.12.9 / git present / uv + repo + API keys missing, and explained the 4-step setup flow

### Agno agent verdict (excerpt)
> youtu-agent is a flexible, high-performance framework for building, running, and evaluating autonomous agents, created by TencentCloudADP. The environment check shows Python 3.12.9 available (meets 3.12+ requirement), git installed, but uv NOT installed, repo not cloned, no LLM API keys configured. The next step to actually use this would be `--setup` to clone the repo and install dependencies.

## Notes

- The original auto-generated client stub required a meaningless `--api-key` flag that was never used. The current bootstrapper uses the proper upstream env var pattern (`UTU_LLM_API_KEY`, etc.) and has honest `--info` reporting.
- Directory was renamed from `youtu_agent` → `youtu-agent` because Agno's `LocalSkills` requires hyphens (no underscores) in skill names.
- The `upstream/` directory created by `--setup` is gitignored.
