from datetime import datetime
from pydantic import BaseModel, validator


def convert_datetime_to_iso_8601_with_z_suffix(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


class SQuestionAnswer(BaseModel):
    question: str
    answer: str
    created_at: datetime

    # @validator("created_at", pre=True)
    # def str_to_datetime(cls, date_time: str) -> datetime:
    #     """
    #     Extract the date from a string like '2004-01-01T00:00:00Z'.
    #     """
    #     date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%f')
    #     return date_time_obj
