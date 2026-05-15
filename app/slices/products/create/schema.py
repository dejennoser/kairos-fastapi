from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    name:str
    description: str
    price: float
    category: str
    stock: int

class CreateProductResponse(BaseModel):
    id: int
    name: str