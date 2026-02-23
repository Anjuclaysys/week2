from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated


class LoginRequest(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=50)]
    password: Annotated[str, Field(min_length=8, max_length=100)]

    @field_validator("username")
    @classmethod
    def username_no_spaces(cls, value):
        if " " in value:
            raise ValueError("Username cannot contain spaces")
        return value

    model_config = {"extra": "forbid"}
