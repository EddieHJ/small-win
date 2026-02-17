from fastapi import APIRouter
# 导入新的模型名
from small_win.schemas.schema import GoalInput, GoalBreakdown
from small_win.core.goal_breakdown import generate_action_plan

router = APIRouter(tags=["AI todo"])

@router.post("/chat", response_model=GoalBreakdown)
async def chat_with_ai(req: GoalInput): # 参数类型变了
    # 字段名变了：从 req.user_input 变成 req.text
    return generate_action_plan(req.text)