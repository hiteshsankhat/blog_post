from fastapi import FastAPI

from .api.api import router

app: FastAPI = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return "Hello World"
