from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import product


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(product.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Product API"}
