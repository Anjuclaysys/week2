# auth/schema.py

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class LoginRequest(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=50)]
    password: Annotated[str, Field(min_length=8, max_length=100)]

    model_config = {"extra": "forbid"}
