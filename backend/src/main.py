from typing import Union

from fastapi import Cookie, Depends, FastAPI

from src import oauth

from .api.api import router

app: FastAPI = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return "Hello World"
