from django.db import models
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = 'postgresql://user:password@localhost:8000/mydatabase'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    amount = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    state = Column(String)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    amount = Column(Integer)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")

Order.items = relationship("OrderItem", order_by=OrderItem.id, back_populates="order")
