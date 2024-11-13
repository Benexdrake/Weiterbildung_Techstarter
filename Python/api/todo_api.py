import json
from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/todo")
async def get_all(request:Request.body):
    #print(request)
    return {"result": ""}