from fastapi import APIRouter
from .schema import CreateProductRequest, CreateProductResponse
from .service import create_product

router = APIRouter()

@router.post("")
def create(data: CreateProductRequest) -> CreateProductResponse:
    product = create_product(data)

    return CreateProductResponse(
        id=product.id,
        name=product.name
    )