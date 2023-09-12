from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict[str, str]:
    return {"message": "It is alive!"}
