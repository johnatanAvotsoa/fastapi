from sqlalchemy import Integer, String, Column, ForeignKey, Table, DateTime, Float  
from sqlalchemy.orm import relationship
from database import Base
import datetime

procuct_purchase = Table(
    'procuct_purchase',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'),primaruy_key=True),
    Column('purchase_id', Integer, ForeignKey('purchases.id'),primary_key=True)
)
class Customer(Base): 
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    purchases = relationship("Purchase", back_populates="owner")

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True,index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('customer.id'))
    owner = relationship("Customer", back_populates="purchases")
    payement_method = Column(String(250), nullable=False)
    amount = Column(Float, nullable=False)
    products = relationship("Product", secondary=procuct_purchase, back_populates="purchases")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(250),nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(250), nullable=False)
    purchases = relationship("Purchase", secondary=procuct_purchase, back_populates="products")