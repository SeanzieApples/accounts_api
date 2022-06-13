from pydantic import BaseModel
from decimal import Decimal


class AccountBase(BaseModel):
    name: str


class DepositWithdraw(BaseModel):
    amount: Decimal

class Account(AccountBase):
    id: int
    balance: Decimal

    class Config:
        orm_mode = True
