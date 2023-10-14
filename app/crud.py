"""CRUD-операции для моделей"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.models import Answer, Question


async def get_last_question() -> str | None:
    stmt = (
        select(Question).order_by(Question.id.desc())
    )
    session: AsyncSession
    async with async_session_maker() as session:
        res = await session.execute(stmt)
        last_question: Question = res.first()
        if not last_question:
            return None
        return last_question.content
