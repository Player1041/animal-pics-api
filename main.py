from random import choice
from glob import glob

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def otters():
    return FileResponse(choice(glob('otters/*')))