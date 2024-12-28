from fastapi import FastAPI
from .database import Base, engine
from .api import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Instagram Backend!"}