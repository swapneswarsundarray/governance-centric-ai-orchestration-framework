from dataclasses import dataclass

@dataclass
class AIResult:
    recommendation: str
    confidence: float
    missing_evidence: bool
