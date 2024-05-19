from fastapi import FastAPI
from rivulet.api import router

app = FastAPI()

app.include_router(router)

def run():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
