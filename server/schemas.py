from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: str
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str
    role: str = "user"

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    customer_name: str
    customer_email: str
    total_amount: float
    payment_method: str
    transaction_id: str
    items: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str

    class Config:
        from_attributes = True
