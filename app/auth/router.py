from fastapi import APIRouter, HTTPException

from app.auth.service import AuthService
from app.auth.schema import LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login")
def login(data: LoginRequest):
    if data.username != "admin" or data.password != "password":
        raise HTTPException(
            detail="Invalid credentials",
        )

    access_token = AuthService.create_access_token({"sub": data.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
