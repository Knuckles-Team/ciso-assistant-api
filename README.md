# Ciso Assistant Api
## MCP

![PyPI - Version](https://img.shields.io/pypi/v/ciso-assistant-api)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/ciso-assistant-api)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/ciso-assistant-api)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/ciso-assistant-api)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/ciso-assistant-api)
![PyPI - License](https://img.shields.io/pypi/l/ciso-assistant-api)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/ciso-assistant-api)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/ciso-assistant-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/ciso-assistant-api)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/ciso-assistant-api)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/ciso-assistant-api)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/ciso-assistant-api)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/ciso-assistant-api)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/ciso-assistant-api)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/ciso-assistant-api)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ciso-assistant-api)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/ciso-assistant-api)

> **Documentation** — Installation, deployment, and usage across the API, CLI, MCP,
> and A2A agent interfaces are maintained in the
> [official documentation](https://knuckles-team.github.io/ciso-assistant-api/).

---

## Overview

CISO Assistant API + MCP Server — 100% API coverage

---

## Installation

```bash
# MCP server with the full medulla engine contract
uv pip install "ciso-assistant-api[mcp]"

# Everything (development)
uv pip install "ciso-assistant-api[all]"      # or: python -m pip install "ciso-assistant-api[all]"
```

### Container images (`:mcp`)

One multi-stage `docker/Dockerfile` builds the MCP-only image (`--target mcp`):

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `${CISO_ASSISTANT_MCP_IMAGE}` | `--target mcp` | `ciso-assistant-api[mcp]` — MCP + `medulla`, no agent runtime | `ciso-assistant-mcp` |

```bash
docker build --target mcp -t "${CISO_ASSISTANT_MCP_IMAGE}" docker/
```

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/ciso-assistant-api/) and is
the recommended reference for installation, deployment, and day-to-day operation.

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=example&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/example)
![GitHub User's stars](https://img.shields.io/github/stars/example)

---

## Contribute

Contributions are welcome! Please ensure code quality by running local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Run test suites using `pytest`
