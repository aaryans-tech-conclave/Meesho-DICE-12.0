from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Integrity Risk Scoring API", version="0.1.0")

class Entity(BaseModel):
    entity_id: str
    entity_type: str  # seller|buyer|listing|device|address

class Signal(BaseModel):
    name: str
    value: float

class RiskRequest(BaseModel):
    entities: List[Entity]
    signals: List[Signal]

class RiskResponse(BaseModel):
    risk_score: float
    reasons: List[str]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score", response_model=RiskResponse)
def score(req: RiskRequest):
    # Placeholder heuristic: average signal value
    score = sum(s.value for s in req.signals) / max(len(req.signals), 1)
    reasons = [f"Aggregated {len(req.signals)} signals"]
    return RiskResponse(risk_score=score, reasons=reasons)
