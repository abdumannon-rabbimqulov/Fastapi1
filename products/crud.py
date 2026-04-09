from fastapi import HTTPException
from products.models import Products
from products.schemas import ProductCreate,ProductUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession



async def create_products(db : AsyncSession, data : ProductCreate):
    product=Products(**data.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def update_product_db(db: AsyncSession, product_id: int, product_update: ProductUpdate):

    result = await db.execute(select(Products).filter(Products.id == product_id))
    db_product = result.scalar_one_or_none()

    if not db_product:
        return None


    update_data = product_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)


    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_all(db:AsyncSession):
    result=await db.execute(select(Products))
    products=result.scalars().all()
    return products


async def get_product(product_id: int, db: AsyncSession):
    result = await db.execute(select(Products).where(Products.id == product_id))
    product = result.scalar_one_or_none()
    return product


async def delete(product_id: int, db: AsyncSession):
    result = await db.execute(select(Products).where(Products.id == product_id))
    db_product = result.scalar_one_or_none()

    await db.delete(db_product)
    await db.commit()
    return None