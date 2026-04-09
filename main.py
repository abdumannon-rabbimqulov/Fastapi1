# from fastapi import FastAPI
# from database import engine, Base
# from products.urls import product_router
# from products.models import Products
#
# app = FastAPI(title="FastAPI CRUD App")
#
# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
# app.include_router(product_router)
#
# @app.get("/")
# def root():
#     return {"message": "Welcome to FastAPI CRUD API"}
