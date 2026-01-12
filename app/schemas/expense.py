from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0)
    category: str
    description: str | None = None