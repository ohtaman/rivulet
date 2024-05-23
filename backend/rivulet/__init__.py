from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from rivulet.api import router


app = FastAPI()
app.include_router(router)
app.mount("/", StaticFiles(directory="rivulet/static", html=True), name="static")
