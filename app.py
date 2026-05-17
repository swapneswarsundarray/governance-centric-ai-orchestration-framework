from models.user_request import UserRequest
from governance.policy_registry import PolicyRegistry
from orchestration.workflow_orchestrator import WorkflowOrchestrator
from orchestration.task_router import TaskRouter
from reasoning.ai_reasoning_engine import AIReasoningEngine
from validation.validation_gate import ValidationGate
from observability.audit_logger import AuditLogger
from rollback.rollback_handler import RollbackHandler


request = UserRequest(
    user_id="case-worker-100",
    task="Analyze disputed transaction",
    risk_tier="high",
    requested_action="recommend_next_step"
)

policy_registry = PolicyRegistry()

if not policy_registry.is_action_allowed(request.requested_action):
    print("❌ Governance blocked action")
    exit()

orchestrator = WorkflowOrchestrator()
orchestrator.start(request)

router = TaskRouter()
router.route(request)

reasoning_engine = AIReasoningEngine()
result = reasoning_engine.generate(request)

validator = ValidationGate()

logger = AuditLogger()
rollback = RollbackHandler()

if validator.validate(result):
    logger.log("approved")
    print("✅ Workflow completed")
else:
    logger.log("validation_failed")
    rollback.rollback()
