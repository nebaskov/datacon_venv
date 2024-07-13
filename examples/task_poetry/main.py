import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def hello():
    return {200: "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
