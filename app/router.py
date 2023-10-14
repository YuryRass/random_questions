import requests
from fastapi import APIRouter

from app.crud import get_last_question

router: APIRouter = APIRouter(
    prefix="/victorina",
    tags=["Get random question"]
)


@router.post("/question")
async def get_random_question(questions_num: int):
    last_question: str = await get_last_question()

    return last_question
