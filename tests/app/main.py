# app/main.py
from fastapi import FastAPI, HTTPException

app = FastAPI(title="FastAPI TDD Example")

# base de dados em memória
_items = {
    1: {"id": 1, "name": "Item 1"},
    2: {"id": 2, "name": "Item 2"},
}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = _items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não existe")
    return item
