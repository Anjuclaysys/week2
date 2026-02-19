import logging

from fastapi import FastAPI

from app.logger import setup_logger
from app.logging_middleware import LoggingMiddleware
from app.routes import router

from app.database import Base, engine
from app import model

app = FastAPI()
setup_logger()
logger = logging.getLogger(__name__)
logger.info("logger is added")

app.add_middleware(LoggingMiddleware)

Base.metadata.create_all(bind=engine)

app.include_router(router)
