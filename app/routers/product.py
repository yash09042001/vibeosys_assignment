from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate, ProductResponse
from sqlalchemy import select

router = APIRouter(prefix="/product", tags=["products"])


@router.get("/list", response_model=List[ProductResponse])
def list_products(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    offset = (page - 1) * per_page
    products = db.execute(
        select(Product).offset(offset).limit(per_page)
    ).scalars().all()
    return products


@router.get("/{pid}/info", response_model=ProductResponse)
def get_product_info(pid: int, db: Session = Depends(get_db)):
    product = db.get(Product, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/add", response_model=ProductResponse, status_code=201)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):

    if db.execute(select(Product
                         ).filter_by(sku=product.sku)).scalar_one_or_none():
        raise HTTPException(status_code=400, detail="SKU already exists")

    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/{pid}/update", response_model=ProductResponse)
def update_product(pid: int,
                   product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.get(Product, pid)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.sku and product.sku != db_product.sku:
        if db.execute(select(Product).filter_by(sku=product.sku)).scalar_one_or_none():
            raise HTTPException(status_code=400, detail="SKU already exists")

    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product
