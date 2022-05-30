import uvicorn

from fastapi import FastAPI

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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8008)
