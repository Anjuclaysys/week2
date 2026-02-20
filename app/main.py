import logging

from dotenv import load_dotenv
from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.core.database import Base, engine
from app.core.logger import setup_logger
from app.core.logging_middleware import LoggingMiddleware
from app.users.routes import router as user_router

load_dotenv()
# print(os.getenv("SECRET_KEY"))

app = FastAPI()


setup_logger()
logger = logging.getLogger(__name__)
logger.info("logger is added")

app.add_middleware(LoggingMiddleware)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(auth_router)
