from app.models.product import Product
from app.core.database import SessionLocal

def create_product(data):
    db = SessionLocal()

    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        category=data.category,
        stock=data.stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()

    return product