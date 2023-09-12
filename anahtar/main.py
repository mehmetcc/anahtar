import uvicorn


def start() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("anahtar.api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
