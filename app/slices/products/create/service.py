from app.models.product import Product

fake_db = []

def create_product(data):
    product = Product(
        id=len(fake_db) + 1,
        name=data.name,
        description=data.description,
        price=data.price,
        category=data.category,
        stock=data.stock
    )

    fake_db.append(product)
    return product