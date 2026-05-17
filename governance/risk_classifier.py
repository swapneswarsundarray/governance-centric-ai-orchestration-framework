class RiskClassifier:

    def classify(self, request):
        if request.risk_tier == "high":
            return "HIGH_RISK"

        return "LOW_RISK"
