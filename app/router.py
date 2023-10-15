from fastapi import APIRouter

from app.crud import add_questions, get_questions
from app.shemas import SQuestionAnswer

router: APIRouter = APIRouter(
    prefix="/victorina",
    tags=["Get random question"]
)


@router.post("/question")
async def get_random_question(questions_num: int):
    questions: list[SQuestionAnswer] = get_questions(questions_num)
    question: str = await add_questions(questions)

    return {'question': question}
