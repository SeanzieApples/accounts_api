from sqlalchemy.orm import Session

from ..schemas import account as schema
from ..models import account as model

def get_account(db: Session, name: str):
    return db.query(model.Account).filter(model.Account.name.ilike(name)).first()

def create_account(db: Session, account: schema.AccountBase):
    db_account = model.Account(name=account.name)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def deposit(db: Session, account: schema.Account, amount: float):
    account.balance += amount
    db.commit()
    db.refresh(account)
    return account


def withdraw(db: Session, account: schema.Account, amount: float):
    account.balance -= amount
    if account.balance < 0:
      account.balance = 0.0
    db.commit()
    db.refresh(account)
    return account
