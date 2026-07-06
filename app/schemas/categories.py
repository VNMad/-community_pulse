from typing import Annotated
from pydantic import BaseModel, ConfigDict, StringConstraints


CategoryName = Annotated[str, StringConstraints(strip_whitespace=True, min_length=2, max_length=100)]


class CategoryBase(BaseModel):
    name: CategoryName


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: CategoryName | None = None


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int