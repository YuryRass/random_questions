"""Класс для конвертирования JSON данных"""
from datetime import datetime
from pydantic import BaseModel


class SQuestionAnswer(BaseModel):
    """
    Структура сгенерированных вопросов и ответов к ним
    """
    question: str
    answer: str
    created_at: datetime
