# Prompt Guard Lab — PRD

## Problem
Prompt injection and jailbreak attempts often share recognizable patterns (roleplay overrides, system prompt exfil, tool misuse). Teams want a quick triage signal before deeper review.

## Goals
- Accept a prompt (and optional context) and return a risk score + reasons.
- Provide a small rule set that is easy to extend.
- Produce an analyst-friendly report.

## Non-goals
- Being a perfect classifier.
- Enforcing policy at runtime (this is a lab tool).

## API
- `POST /api/guard/score`

## UX (Streamlit)
- Paste a prompt.
- View score + matched rules.

## Sources
- Hugging Face — AprielGuard: https://huggingface.co/blog/ServiceNow-AI/aprielguard
