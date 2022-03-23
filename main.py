from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import random

app = FastAPI()


@app.get("/random")
async def random_otter():
    return FileResponse('otters/' + (random.choice(os.listdir("otters")))