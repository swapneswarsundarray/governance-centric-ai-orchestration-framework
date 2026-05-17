from models.ai_result import AIResult

class AIReasoningEngine:

    def generate(self, request):
        print("🤖 Generating AI recommendation")

        return AIResult(
            recommendation="Recommend manual review",
            confidence=0.72,
            missing_evidence=True
        )
