from sqlalchemy import Column, BigInteger, String, Integer, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import enum


Base = declarative_base()


class ProductCategory(enum.Enum):
    FINISHED = "finished"
    SEMI_FINISHED = "semi-finished"
    RAW = "raw"


class UnitOfMeasure(enum.Enum):
    MTR = "mtr"
    MM = "mm"
    LTR = "ltr"
    ML = "ml"
    CM = "cm"
    MG = "mg"
    GM = "gm"
    UNIT = "unit"
    PACK = "pack"


class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(ProductCategory), nullable=False)
    description = Column(String(250))
    product_image = Column(String(65535))
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(Enum(UnitOfMeasure), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(DateTime, server_default=func.now(),
                          onupdate=func.now())
