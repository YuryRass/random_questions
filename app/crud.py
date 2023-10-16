"""CRUD-операции для моделей"""
import requests
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.models import Answer, Question
from app.shemas import SQuestionAnswer
from app.config import settings


async def add_questions(
    data: list[SQuestionAnswer]
) -> str | None:
    """Функция заполняет модели Question и Answer

    Args:
        data (list[SQuestionAnswer]):
            данные для инициализации моделей
    """
    session: AsyncSession
    answers: list[Answer] = []
    is_questions_empty: bool = await check_questions_empty()

    async with async_session_maker() as session:
        for it in data:
            if not await find_question(it.question):
                question: Question = Question(
                    content=it.question,
                    created_at=it.created_at
                )
                answer: Answer = Answer(
                    content=it.answer,
                    question=question
                )
                answers.append(answer)
            else:
                answer: Answer = await get_answer_with_unicue_question()
                answers.append(answer)

        session.add_all(answers)
        await session.commit()

    if len(answers) == 1 and not is_questions_empty:
        res: str | None = await get_last_question()
        return res
    elif len(answers) > 1:
        return answers[-2].question.content
    else:
        return None


async def check_questions_empty() -> bool:
    """Проверяет пуста ли таблица Question

    Returns:
        bool: если пуста - True
    """
    stmt = select(Question)
    session: AsyncSession
    async with async_session_maker() as session:
        res = await session.execute(stmt)
        return not res.first()


async def get_answer_with_unicue_question() -> Answer:
    """Функция возвращает объет Answer с уникальным вопросом

    Returns:
        Answer
    """
    payload = {"count": 1}

    # цикл выполняется, пока не найдется уникальный вопрос
    while True:
        resp = requests.get(settings.URL, params=payload)

        data: SQuestionAnswer = SQuestionAnswer(**resp.json()[0])
        question_content: str = data.question

        question: Question | None = await find_question(question_content)
        if not question:
            unicue_question: Question = Question(
                content=question_content,
                created_at=data.created_at
            )
            answer: Answer = Answer(
                content=data.answer,
                question=unicue_question
            )
            return answer


async def find_question(question: str) -> Question | None:
    """Возвращает объект класса Question, если он имеется

    Args:
        question (str): содержимое вопроса

    Returns:
        Question | None
    """
    session: AsyncSession
    async with async_session_maker() as session:
        stmt = (
            select(Question).where(Question.content == question)
        )

        res = await session.execute(stmt)

        return res.scalar_one_or_none()


async def get_last_question() -> str | None:
    """Функция возвращает последний вопрос, который
    присутствует в таблице question

    Returns:
        str | None: содержимое вопроса
    """
    stmt = (
        select(Question).order_by(Question.id.desc())
    )
    session: AsyncSession
    async with async_session_maker() as session:
        res = await session.execute(stmt)
        last_question: Question | None = res.scalar()
        if not last_question:
            return None
        return last_question.content


def get_questions(num_question: int) -> list[SQuestionAnswer]:
    """Генерирует вопросы, обращаясь к публичному API

    Args:
        num_question (int): кол-во вопросов

    Returns:
        list[SQuestionAnswer]: списко сгенерированных вопросов
    """
    payload = {"count": num_question}
    data = requests.get(settings.URL, params=payload).json()

    questions: list[SQuestionAnswer] = []

    for it in data:
        questions.append(
            SQuestionAnswer(**it)
        )

    return questions
