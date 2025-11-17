from sqlalchemy import Column, Integer, String
from .db import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_type = Column(String)
    monthly_usage = Column(Integer)
    debt_amount = Column(Integer)
