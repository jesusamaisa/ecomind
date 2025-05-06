from fastapi import FastAPI
from routes import router

app = FastAPI(title="EcoMind API", version="1.0")

# Tüm route'ları bağla
app.include_router(router)