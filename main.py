from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import random

app = FastAPI()

@app.get("/random")
async def random():
    return FileResponse(random.choice(os.listdir("otters")))