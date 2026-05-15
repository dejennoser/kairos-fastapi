from app.models.product import Product
from app.core.database import SessionLocal

def list_products():
    db = SessionLocal()

    products = db.query(Product).all()

    db.close()

    return products
