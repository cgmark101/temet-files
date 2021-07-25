from fastapi import FastAPI, Request
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers import ping
from models.hellow import Hellow

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/hello')
async def welcome(hello:Hellow):
    return hello

app.include_router(ping.route)