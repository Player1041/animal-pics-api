from random import choice
from glob import glob

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def site(response_class=HTMLResponse):
    return FileResponse("index.html")


@app.get("/otters")
async def otter():
    return FileResponse(choice(glob('otters/*')))