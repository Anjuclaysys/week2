import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app import model
from app.database import Base, engine
from app.logger import setup_logger
from app.logging_middleware import LoggingMiddleware
from app.routes import router

load_dotenv()
# print(os.getenv("SECRET_KEY"))

app = FastAPI()


setup_logger()
logger = logging.getLogger(__name__)
logger.info("logger is added")

app.add_middleware(LoggingMiddleware)

Base.metadata.create_all(bind=engine)

app.include_router(router)
