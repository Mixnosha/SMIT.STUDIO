from tortoise import Tortoise
from config import DB_HOST, DB_PASS, DB_USER, DB_NAME, DB_PORT

DATABASE_URL = f"asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


async def connect_to_db() -> None:
    await Tortoise.init(db_url=DATABASE_URL, modules={"models": ["rate.models"]})
