from fastapi import APIRouter

route = APIRouter()

@route.get('/ping')
async def pong():
    return 'pong'