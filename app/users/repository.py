from sqlalchemy.orm import Session

from app.users import model
from app.users.schema import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        """
        Create a new user in the database.

        :param db:Active database session.
        :type db: session
        :param user: Pydantic schema containing user creation data.
        :type user: UserCreate
        """
        db_user = model.User(
            name=user.name,
            email=user.email,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        """
        Retrieve a user by ID.

        :param db: Active database session.
        :type db: session
        :param user_id: ID of the user to retrieve.
        :type user_id: int
        """
        return self.db.query(model.User).filter(model.User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(model.User).filter(model.User.email == email).first()

    def update_user(self, user_id: int, user: UserUpdate):
        """
        Update an existing user's information.

        :param db:Active database session.
        :type db: session
        :param user_id: ID of the user to update.
        :type user_id: int
        :param user: Pydantic schema containing updated fields.
        :type user: UserUpdate
        """
        db_user = self.get_user(user_id)

        if not db_user:
            return None

        if user.name is not None:
            db_user.name = user.name
        if user.email is not None:
            db_user.email = user.email

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        """
        Delete a user from the database.

        :param db: Active database session.
        :type db: session
        :param user_id: Description
        :type user_id: ID of the user to delete.
        """
        # user = self.query(model.User).filter(
        # model.User.id == user_id).first()
        user = self.get_user(user_id)
        if not user:
            return None

        self.db.delete(user)
        self.db.commit()

        return user
