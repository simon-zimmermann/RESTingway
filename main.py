from typing import Union
import json
from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    api_url = "https://xivapi.com/search"
    data = {
        "indexes": "Item",
        "columns": "ID,NameCombined_en,Name,Name_en",
        "body": {
            "query": {
                "bool": {
                    "must": [
                        {
                            "wildcard": {
                                "NameCombined_en": "*skybu*"
                            }
                        }
                    ]
                }
            }
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, json=data)
        return response.json()


@app.get("/sky")
async def read_sky():
    api_url = "https://xivapi.com/Item/28063"

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


