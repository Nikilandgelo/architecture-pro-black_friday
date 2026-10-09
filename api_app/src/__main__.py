from uvicorn import run

if __name__ == "__main__":
    run("src.app:app", host="0.0.0.0", port=8080)
