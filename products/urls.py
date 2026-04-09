from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import get_db
from products.schemas import ProductCreate, ProductUpdate, ProductResponse
from products.crud import (create_products,
                update_product_db,get_all,
                get,delete
                )



product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post("/create", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_new_product(data: ProductCreate, db: AsyncSession = Depends(get_db)):
    new_product= await create_products(db=db, data=data)
    if not new_product:
        raise HTTPException(status_code=400, detail="Mahsulot yaratishda xatolik!")

    return new_product

@product_router.get("/", response_model=List[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    products=await get_all(
        db=db
    )

    return products

@product_router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await get(
        product_id=product_id,
        db=db
    )
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product





@product_router.put("/{product_id}", response_model=ProductResponse)
async def update(
        product_id: int,
        product_update: ProductUpdate,
        db: AsyncSession = Depends(get_db)
):
    # Logikani CRUD qatlamiga topshiramiz
    db_product = await update_product_db(
        db=db,
        product_id=product_id,
        product_update=product_update
    )


    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return db_product

@product_router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product =await delete(
        product_id=product_id,
        db=db
    )
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
