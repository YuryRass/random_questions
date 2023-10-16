"""Модуль по созданию подключения к БД"""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine, AsyncSession,
    async_sessionmaker, create_async_engine
)
from config import settings

engine: AsyncEngine = create_async_engine(url=settings.DATABASE_URL)

async_session_maker: AsyncSession = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    ...
