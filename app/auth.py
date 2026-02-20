import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError

SECRET_KEY = os.getenv("SECRET_KEY")
# SECRET_KEY = "supersecretkey"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()


def create_access_token(data: dict):
    """
    Create a signed JWT access token

    :param data: Payload data to include in the token.
                     Typically contains user identifier
    :type data: dict
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    """
    Verify and decode a JWT token.

    :param token: Encoded JWT token.
    :type token: str
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return None


def current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    FastAPI dependency to retrieve the current authenticated user.

    :param credentials: Extracts the Bearer token from the Authorization header,
                        verifies it, and returns the username
                        stored in the "sub" claim.
    :type credentials: HTTPAuthorizationCredentials
    """
    token = credentials.credentials
    payload = verify_token(token)
    print("TOKEN RECEIVED:", token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid or expired token",
        )
    return payload.get("sub")
