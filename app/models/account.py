
from sqlalchemy import Column, Float, Integer, String, Index, func
from ..db.database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
Index('account_name_index', func.lower(Account.name), unique=True)