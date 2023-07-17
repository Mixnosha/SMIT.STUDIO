import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from rate.router import router as post_router
from tortoise.contrib.fastapi import register_tortoise
from database import DATABASE_URL

app = FastAPI(title="SMIT.STUDIO")

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["rate.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = APIRouter(prefix="/api/v1")

routers.include_router(post_router)


app.include_router(routers)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
