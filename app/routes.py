from fastapi import APIRouter, HTTPException
from app.schema import UserCreate, UserResponse, UserUpdate
from app.db import user_db

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Server running"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    user_id = len(user_db) + 1

    user_db[user_id] = {"id": user_id, **user.model_dump()}
    print(user_db[user_id])

    return user_db[user_id]


@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    if id not in user_db:
        raise HTTPException(status_code=404, detail="user not found")
    return user_db[id]


@router.put("/users/{id}", response_model=UserResponse)
def update_user(id: int, user: UserUpdate):
    if id not in user_db:
        raise HTTPException(status_code=404, detail="User not found")
    stored_user = user_db[id]

    if user.name is not None:
        stored_user["name"] = user.name
    if user.email is not None:
        stored_user["email"] = user.email

    user_db[id] = stored_user
    return stored_user
