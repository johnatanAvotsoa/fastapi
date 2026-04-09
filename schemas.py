from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    price: int
    category: str

class CustomerCreate(BaseModel):
    name: str
    email: str
class CustomerResponse(BaseModel):
    id:int
    class config:
        from_attribute = True
class PurchaseCreate(BaseModel):
    owner_id: int
    payement_method: str
    amount: float
    products: List[int]  # List of product IDs

