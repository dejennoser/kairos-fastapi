from fastapi import FastAPI

from app.models.product import Base
from app.core.database import engine

from app.slices.products.create.router import router as create_router
from app.slices.products.list.router import router as list_router

app = FastAPI(title="Kairos FastAPI V2")

# ✅ ensure tables are created AFTER app starts
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# ✅ routes
app.include_router(create_router, prefix="/api/v2/products")
app.include_router(list_router, prefix="/api/v2/products")


@app.get("/")
def root():
    return {"message": "kairos FastAPI running"}