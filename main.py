from fastapi import FastAPI, Response, Path, Query, Body
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse, FileResponse
from method.users import users_router
from models.structure import User
from typing import Union, Annotated

app = FastAPI()

app.include_router(users_router)

@app.get('/', response_class=PlainTextResponse)
def f_indexH():
    return "Hello, User!"


