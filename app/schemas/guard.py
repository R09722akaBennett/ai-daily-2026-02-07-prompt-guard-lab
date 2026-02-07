from __future__ import annotations

from pydantic import BaseModel, Field


class GuardRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=12000)
    context: str | None = Field(None, max_length=8000)


class RuleHit(BaseModel):
    rule_id: str
    description: str
    evidence: str
    weight: int


class GuardResponse(BaseModel):
    score: int
    level: str
    hits: list[RuleHit]
