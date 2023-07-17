from tortoise import Tortoise, run_async
from database import connect_to_db


async def init():
    await connect_to_db()
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
