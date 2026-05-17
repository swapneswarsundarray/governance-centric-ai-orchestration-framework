class PolicyRegistry:

    def __init__(self):
        self.blocked_actions = {
            "approve_refund_without_review",
            "update_ledger_directly"
        }

    def is_action_allowed(self, action: str) -> bool:
        return action not in self.blocked_actions
