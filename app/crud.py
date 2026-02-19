from sqlalchemy.orm import session

from app import model
from app.schema import UserCreate, UserUpdate


def create_user(db: session, user: UserCreate):
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

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: session, user_id: int):
    """
    Retrieve a user by ID.

    :param db: Active database session.
    :type db: session
    :param user_id: ID of the user to retrieve.
    :type user_id: int
    """
    return db.query(model.User).filter(model.User.id == user_id).first()


def update_user(db: session, user_id: int, user: UserUpdate):
    """
    Update an existing user's information.

    :param db:Active database session.
    :type db: session
    :param user_id: ID of the user to update.
    :type user_id: int
    :param user: Pydantic schema containing updated fields.
    :type user: UserUpdate
    """
    db_user = get_user(db, user_id)

    if not db_user:
        return None

    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: session, user_id: int):
    """
    Delete a user from the database.

    :param db: Active database session.
    :type db: session
    :param user_id: Description
    :type user_id: ID of the user to delete.
    """
    user = db.query(model.User).filter(model.User.id == user_id).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user
