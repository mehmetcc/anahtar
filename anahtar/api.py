from anahtar.models import TextRequest, TextResponse
from anahtar.tokens import keywords
from fastapi import FastAPI


app: FastAPI = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict[str, str]:
    return {"message": "It is alive!"}


@app.post("/text/", tags=["text"])
async def read_text(request: TextRequest) -> TextResponse:
    return TextResponse(keywords=keywords(request.text))
