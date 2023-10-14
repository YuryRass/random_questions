"""Модели 'Вопросы и Ответы'"""
from datetime import datetime
from sqlalchemy import ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Question(Base):
    "Вопросы для викторины"
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(
        Text, unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(DateTime)
    answer_id: Mapped[int] = mapped_column(
        ForeignKey("answer.id", ondelete='CASCADE'),
        nullable=False,
    )
    # answer: Mapped["Answer"] = relationship(
    #     back_populates="question",
    # )


class Answer(Base):
    "Ответы для викторины"
    __tablename__ = 'answer'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
