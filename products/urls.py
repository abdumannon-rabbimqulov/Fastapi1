from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from database import get_db
from products.models import Products
from products.schemas import ProductCreate, ProductUpdate, ProductResponse
from products.crud import create_products


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_new_product(data: ProductCreate, db: AsyncSession = Depends(get_db)):
    new_product= await create_products(db=db, data=data)
    if not new_product:
        raise HTTPException(status_code=400, detail="Mahsulot yaratishda xatolik!")

    return new_product

@product_router.get("/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products))
    products = result.scalars().all()
    return products

@product_router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_update: ProductUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == product_id))
    db_product = result.scalar_one_or_none()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
        
    await db.commit()
    await db.refresh(db_product)
    return db_product

@product_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Products).where(Products.id == product_id))
    db_product = result.scalar_one_or_none()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    await db.delete(db_product)
    await db.commit()
    return None
