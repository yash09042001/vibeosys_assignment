from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime
from app.models import ProductCategory, UnitOfMeasure


class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    category: ProductCategory
    description: Optional[str] = Field(None, max_length=250)
    product_image: Optional[HttpUrl] = None
    sku: str = Field(..., max_length=100)
    unit_of_measure: UnitOfMeasure
    lead_time: int = Field(..., ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None, max_length=100)
    sku: Optional[str] = Field(None, max_length=100)
    lead_time: Optional[int] = Field(None, ge=0)


class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
