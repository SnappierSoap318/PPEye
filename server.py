from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return json.load(open('data.json'))