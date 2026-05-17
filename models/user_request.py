from dataclasses import dataclass

@dataclass
class UserRequest:
    user_id: str
    task: str
    risk_tier: str
    requested_action: str
