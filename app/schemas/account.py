from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str


class DepositWithdraw(BaseModel):
    amount: float

class Account(AccountBase):
    id: int
    balance: float

    class Config:
        orm_mode = True
