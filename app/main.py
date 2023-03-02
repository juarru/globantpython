from fastapi import FastAPI
from .router.weather_router import router

app = FastAPI()
app.include_router(router)
