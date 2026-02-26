from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated


class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]

    email: EmailStr

    model_config = {"extra": "forbid"}


class UserUpdate(BaseModel):
    name: Optional[Annotated[str, Field(min_length=2, max_length=50)]] = None
    email: Optional[EmailStr] = None

    model_config = {"extra": "forbid"}


class UserResponse(UserBase):
    id: int

    model_config = {"from_attributes": True}
