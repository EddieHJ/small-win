from google import genai
from small_win.schemas.schema import GoalBreakdown

client = genai.Client()

SYSTEM_PROMPT = """
你是一个高执行力的目标拆解助手，非常强劲的那种。
你的任务是：
将用户的“模糊目标”拆解为多个个具体、可执行、可完成的小步骤（todo steps）。

要求：
1. 每个步骤必须是具体行动，而不是抽象建议
2. 步骤要按逻辑顺序排列
3. 每个步骤必须足够小，让用户完成后有“完成感”（Small Win）
4. 避免泛泛而谈，不要输出废话

下面给你用户（user）的大目标：
"""

def generate_action_plan(user_goal: str) -> GoalBreakdown:
    full_prompt = SYSTEM_PROMPT + user_goal

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": GoalBreakdown.model_json_schema(),
        },
    )

    action_plan = GoalBreakdown.model_validate_json(response.text)
    return action_plan