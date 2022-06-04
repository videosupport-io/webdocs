from typing import List

import uvicorn

from fastapi import FastAPI, HTTPException

from src.scrapper import scrap_paragraphs

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping")
def read_root():
    return 'pong'


@app.get('/get_paragraphs')
def get_paragraphs(url: str):
    return {
        'paragraphs': scrap_paragraphs(url)
    }


@app.post('/get_paragraph_by_index')
def get_paragraph_by_index(url: str, indexes: List[int]):
    paragraphs = scrap_paragraphs(url)
    if any(id > len(paragraphs) for id in indexes):
        raise HTTPException(status_code=400, detail='index greater than paragraphs length')
    return [{id: paragraphs[id]} for id in indexes]


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8008)
