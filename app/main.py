from fastapi import FastAPI

from app.api import v1

app = FastAPI()


@app.get("/")
async def index():
    return b"Hello, World!"


app.include_router(v1.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", port=5000, reload=True)
