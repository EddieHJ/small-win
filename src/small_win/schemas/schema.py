from pydantic import BaseModel, Field, ConfigDict

class GoalInput(BaseModel):
    """
    接收用户提交的目标描述。
    """
    # Pydantic V2 配置：自动去除字符串首尾的空格
    model_config = ConfigDict(str_strip_whitespace=True)

    text: str = Field(
        ...,
        min_length=2,
        max_length=2000,
        title="目标描述",
        description="用户想要拆解的模糊大目标（建议 2-200 字）。",
        examples=["我想在三个月内学会Python数据分析"]
    )

# 顺便把之前讨论的 Output 模型也放进来，保持文件完整性
class ActionStep(BaseModel):
    instruction: str = Field(description="一个具体、可执行的小任务。")
    order: int = Field(description="此步骤的执行顺序。")

class GoalBreakdown(BaseModel):
    objective: str = Field(description="被AI优化和提炼后的主目标描述。")
    steps: list[ActionStep] = Field(description="为实现目标而拆解出的行动步骤列表。")
    summary: str = Field(description="对整个行动计划的简短总结。")