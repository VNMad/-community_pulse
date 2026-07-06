from pydantic import BaseModel, ConfigDict
from app.models import Statistics
from app.schemas import *


class QuestionCreateRequest(QuestionCreate):
    pass


class QuestionUpdateRequest(QuestionUpdate):
    pass

class QuestionResponse(QuestionRead):
    category: CategoryRead


class QuestionDetailResponse(QuestionRead):
    category: CategoryRead
    statistics: StatisticsRead | None = None


class QuestionListResponse(BaseModel):
    items: list[QuestionResponse]
    count: int
