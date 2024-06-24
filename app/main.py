from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Dev FastAPI pet project"
)

app.include_router(router, prefix="/api")
