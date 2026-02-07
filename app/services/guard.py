from __future__ import annotations

import re


_RULES: list[tuple[str, str, int, list[str]]] = [
    (
        "sys_override",
        "Attempts to override system/developer instructions",
        5,
        [
            r"ignore (all|any|previous) instructions",
            r"disregard (the )?system",
            r"you are now (dan|developer mode)",
        ],
    ),
    (
        "exfiltrate",
        "Requests hidden prompts / secrets / tokens",
        6,
        [
            r"system prompt",
            r"reveal.*(secret|token|key)",
            r"print.*(api key|token)",
        ],
    ),
    (
        "tool_misuse",
        "Attempts to trigger tools or side effects",
        4,
        [
            r"run this command",
            r"curl ",
            r"rm -rf",
        ],
    ),
    (
        "roleplay",
        "Roleplay framing to bypass safeguards",
        3,
        [
            r"let's roleplay",
            r"pretend you are",
            r"as an unfiltered model",
        ],
    ),
]


def score_prompt(prompt: str, context: str | None = None) -> tuple[int, str, list[dict]]:
    text = (prompt + "\n" + (context or "")).lower()
    hits: list[dict] = []
    score = 0

    for rule_id, desc, weight, patterns in _RULES:
        for pat in patterns:
            m = re.search(pat, text)
            if m:
                evidence = text[max(0, m.start() - 40) : m.end() + 40]
                hits.append(
                    {
                        "rule_id": rule_id,
                        "description": desc,
                        "evidence": evidence.strip(),
                        "weight": weight,
                    }
                )
                score += weight
                break

    if score >= 10:
        level = "high"
    elif score >= 5:
        level = "medium"
    else:
        level = "low"

    return score, level, hits
