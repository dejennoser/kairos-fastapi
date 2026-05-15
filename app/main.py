from fastapi import FastAPI
from app.slices.products.create.router import router as create_router

from app.slices.products.list.router import router as list_router

app = FastAPI(title="Kairos FastAPI V2")


app.include_router(create_router, prefix="/api/v2/products")


@app.get("/")
def root():
    return {"message": "kairos FastAPI running"}

app.include_router(list_router, prefix="/api/v2/products")