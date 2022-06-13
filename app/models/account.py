
from sqlalchemy import Column, Numeric, Integer, String, Index, func
from sqlalchemy.orm import validates
from ..db.database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    balance = Column(Numeric(13, 2), nullable=False, default=0.0 )

    @validates('balance')
    def validate_balance(self, key, balance):
        if balance < 0:
            raise ValueError("Balance can not go below 0.00")
        return balance

Index('account_name_index', func.lower(Account.name), unique=True)