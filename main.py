from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import random

random_otter = random.choice(os.listdir("otters"))
app = FastAPI()

@app.get("/")
async def random():
    return random_otter