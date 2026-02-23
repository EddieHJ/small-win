from fastapi import APIRouter, HTTPException
# 导入新的模型名
from small_win.schemas.schema import GoalInput, GoalBreakdown
from small_win.core.goal_breakdown import generate_action_plan

router = APIRouter(tags=["AI todo"])

@router.post("/chat", response_model=GoalBreakdown)
async def chat_with_ai(req: GoalInput): # 函数名建议改得更有语义
    """
    接收用户目标，调用 AI 生成拆解计划。
    """
    try:
        # 关键修改：加上 await
        result = await generate_action_plan(req.text)
        return result
    except Exception as e:
        # 优雅地返回错误给前端，而不是直接 500 崩溃
        raise HTTPException(
            status_code=500,
            detail=f"AI 服务暂时不可用: {str(e)}"
        )