import random
import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/quotes")
def get_quotes():
    with open("quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)

    return {
        "quote": random.choice(quotes["quotes"])
    }
