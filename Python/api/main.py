from fastapi import FastAPI
from todo_api import router

app = FastAPI()

@app.get("/")
async def root():
    return "Todo App"

app.include_router(router)