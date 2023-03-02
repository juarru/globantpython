from fastapi import FastAPI
from .v1.router.weather_router import router

app = FastAPI()
app.include_router(router)
