class ValidationGate:

    def validate(self, result):

        if result.confidence < 0.85:
            print("❌ Validation failed: low confidence")
            return False

        if result.missing_evidence:
            print("❌ Validation failed: missing evidence")
            return False

        print("✅ Validation passed")
        return True
