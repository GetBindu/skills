---
name: youtu-agent
description: Flexible framework from TencentCloudADP for building, running, and evaluating autonomous agents. Requires cloning the upstream repo and an LLM API key (DeepSeek, OpenAI, etc.).
metadata:
    source_type: github
    repository_url: https://github.com/TencentCloudADP/youtu-agent
    reference_url: https://arxiv.org/abs/2512.24615
---

# youtu_agent

Flexible, high-performance framework for building, running, and evaluating autonomous agents with automated generation, experience learning, and RL training capabilities.

- **Code**: https://github.com/TencentCloudADP/youtu-agent
- **Paper**: https://arxiv.org/abs/2512.24615

## What This Skill Provides

This skill is a **bootstrapper** for the upstream TencentCloudADP/youtu-agent repo. It:

1. Clones the upstream repo into `upstream/youtu-agent/`
2. Installs its dependencies via `uv sync`
3. Runs the agent CLI with your config

It does **not** bundle the framework itself — that lives in the upstream repo.

## Quick Start

### 1. Check environment
```bash
cd {baseDir}
python3 scripts/youtu_agent_client.py --info
```

This reports whether git, uv, the cloned repo, and required API keys are ready.

### 2. Set up (clone repo + install dependencies)
```bash
python3 scripts/youtu_agent_client.py --setup
```

Requires `git` and `uv`. Install uv with:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Configure LLM credentials
Export environment variables before running:
```bash
export UTU_LLM_API_KEY="your-api-key"
export UTU_LLM_MODEL="deepseek-chat"
export UTU_LLM_BASE_URL="https://api.deepseek.com/v1"
```

Supported providers (any OpenAI-compatible endpoint):
- **DeepSeek**: `https://api.deepseek.com/v1`
- **Tencent Cloud DeepSeek**: `https://api.lkeap.cloud.tencent.com/v1`
- **OpenAI**: `https://api.openai.com/v1`

Optional tool keys for web search:
```bash
export SERPER_API_KEY="..."   # for web search
export JINA_API_KEY="..."     # for web reading
```

### 4. Run an agent
```bash
python3 scripts/youtu_agent_client.py --config simple/base
# or with web search
python3 scripts/youtu_agent_client.py --config simple/base_search
```

The bootstrapper delegates to the upstream `scripts/cli_chat.py` with the provided config.

## Available Configs (from upstream)

- `simple/base` — Basic agent, no internet
- `simple/base_search` — Agent with web search tools
- `ww` — WebWalkerQA evaluation config

See `upstream/youtu-agent/configs/agents/` after setup for the full list.

## One-liner (full setup + first run)

```bash
cd {baseDir} && \
  python3 scripts/youtu_agent_client.py --setup && \
  UTU_LLM_API_KEY=sk-... UTU_LLM_MODEL=deepseek-chat UTU_LLM_BASE_URL=https://api.deepseek.com/v1 \
  python3 scripts/youtu_agent_client.py --config simple/base
```

## Script Parameters

| Flag | Description |
|------|-------------|
| `--info` | Report environment status (git, uv, repo, env vars) |
| `--setup` | Clone upstream repo and install dependencies |
| `--config <name>` | Run the specified agent config |
| `--format {json,summary}` | Output format for status (default: json) |

## Required Dependencies

- **Python 3.12+** (for the upstream framework itself)
- **git** (to clone the repo)
- **uv** (for upstream dependency management)
- **LLM API key** (DeepSeek, OpenAI, or OpenAI-compatible)

## What Lives Where

```
youtu_agent/
├── SKILL.md                          # This file
├── scripts/
│   └── youtu_agent_client.py         # Bootstrapper (clone + install + run)
├── references/
│   └── usage_guide.md                # Reference documentation
└── upstream/                         # Created by --setup
    └── youtu-agent/                  # Cloned upstream repo
        ├── scripts/cli_chat.py       # Actual CLI entry point
        ├── configs/                  # Agent YAML configs
        └── examples/                 # Example agents
```

## Citation

If you use youtu_agent in research, cite the paper: https://arxiv.org/abs/2512.24615
