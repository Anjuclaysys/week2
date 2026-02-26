from app.users.repository import UserRepository
from app.users.schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data: UserCreate):
        existing_user = self.repository.get_user_by_email(user_data.email)

        if existing_user:
            raise ValueError("user aleady exists")

        return self.repository.create_user(user_data)

    def get_user(self, user_id: int):
        return self.repository.get_user(user_id)

    def update_user(self, user_id: int, user_data: UserUpdate):
        return self.repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int):
        return self.repository.delete_user(user_id)
