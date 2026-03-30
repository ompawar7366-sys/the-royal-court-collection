from sqlalchemy import Column, Integer, String, Float, Text

from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(Text)
    price = Column(Float)
    category = Column(String(50))
    image_url = Column(Text)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100)) # In a real app, use hashing!
    role = Column(String(20), default="user") # 'admin' or 'user'

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    customer_email = Column(String(100))
    total_amount = Column(Float)
    payment_method = Column(String(50))
    transaction_id = Column(String(100), unique=True, index=True)
    status = Column(String(50), default="pending")
    items = Column(Text) # JSON string of items
