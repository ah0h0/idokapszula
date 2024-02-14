from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    print(f'q:{q}')
    return {'item': item_id, 'q': q}
