import nltk
import uvicorn


def launch_nltk() -> None:
    print("Downloading NLTK - Punkt model")
    nltk.download("punkt")


def launch_server() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("anahtar.api:app", host="0.0.0.0", port=8000, reload=True)


def start() -> None:
    launch_nltk()
    launch_server()


if __name__ == "__main__":
    start()
