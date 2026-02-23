from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.users.repository import UserRepository
from app.users.schema import UserCreate, UserResponse, UserUpdate
from app.users.service import UserService


router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)


@router.get("/")
def root():
    return {"message": "Server running"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, this is a protected route"}


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):

    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(detail=str(e))


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.put("/{id}", response_model=UserResponse)
def update_user(
    id: int, user: UserUpdate, service: UserService = Depends(get_user_service)
):
    updated_user = service.update_user(id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/{id}", response_model=UserResponse)
def delete_user(id: int, service: UserService = Depends(get_user_service)):
    deleted_user = service.delete_user(id)

    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    return deleted_user
