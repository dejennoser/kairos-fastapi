from fastapi import APIRouter
from .service import list_products
from .schema import ProductResponse

router = APIRouter()

@router.get("")
def get_all():
    products = list_products()

    return [
        ProductResponse(
            id=p.id,
            name=p.name,
            price=p.price
        )
        for p in products
    ]
