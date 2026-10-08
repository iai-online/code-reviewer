# code-reviewer

An AI-powered code reviewer that analyzes git diffs and provides detailed feedback.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- An [Anthropic API key](https://console.anthropic.com/)

## Getting Started

**1. Clone and install dependencies**

```bash
git clone <repo-url>
cd code-reviewer
uv sync
```

**2. Set up your API key**

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

**3. Run a review**

Pass a diff file as an argument:

```bash
uv run src/review.py path/to/your.diff
```

To review a demo diff:

```bash
uv run src/review.py demos/diffs/day01.diff
```

To review your current git changes:

```bash
git diff > changes.diff
uv run src/review.py changes.diff
```

## Progress Log

| Tag | Changes |
|-----|---------|
| [v0.1.0](https://github.com/pradnya-git-dev/code-reviewer/releases/tag/v0.1.0) | Initial project setup |
