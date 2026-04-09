from fastapi import HTTPException
from sqlalchemy.orm import Session
from products.models import Products
from products.schemas import ProductCreate

async def create_products(db : Session, data : ProductCreate):
    product=Products(**data.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product
