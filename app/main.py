"""Веб-сервис random_questions"""
from fastapi import FastAPI
from app.router import router


app: FastAPI = FastAPI()
app.include_router(router)
