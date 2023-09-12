from fastapi import FastAPI
from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    keywords: list[str]
