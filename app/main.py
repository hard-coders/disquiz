from functools import lru_cache

from fastapi import FastAPI

from app.api import v1
from app.models import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
async def index():
    return b"Hello, World!"


app.include_router(v1.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", port=5000, reload=True)
