from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session

from app.auth import create_access_token, current_user
from app.database import get_db
from app import crud
from app.schema import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Server running"}


@router.get("/health")
def health():
    return {"status": "healthy"}


@router.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "password":
        raise HTTPException(status_code=401, detail="invalid credentials")
    access_token = create_access_token({"sub": username})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected")
def protected_route(current_user: str = Depends(current_user)):
    return {"message": f"Hello {current_user},this is a protected route"}


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: session = Depends(get_db)):
    user = crud.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.put("/users/{id}", response_model=UserResponse)
def update_user(id: int, user: UserUpdate, db: session = Depends(get_db)):
    updated_user = crud.update_user(db, id, user)
    if not update_user:
        raise HTTPException(status_code=404, detail="User not found")

    return update_user


@router.delete("/users/{id}", response_model=UserResponse)
def delete_user(id: int, db: session = Depends(get_db)):
    deleted_user = crud.delete_user(db, id)

    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    return deleted_user
