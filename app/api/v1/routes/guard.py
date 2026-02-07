from __future__ import annotations

from fastapi import APIRouter

from app.schemas.guard import GuardRequest, GuardResponse, RuleHit
from app.services.guard import score_prompt

router = APIRouter(prefix='/guard')


@router.post('/score', response_model=GuardResponse)
def score(req: GuardRequest) -> GuardResponse:
    score, level, hits = score_prompt(req.prompt, req.context)
    return GuardResponse(score=score, level=level, hits=[RuleHit(**h) for h in hits])
