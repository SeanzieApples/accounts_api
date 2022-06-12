from urllib import response
from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from ..schemas import account as schema
from ..crud import account as crud
from ..db.database import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("", status_code=201)
def create_account(account: schema.AccountBase, db: Session = Depends(get_db)):
    '''
    Creates an account with the given name
    
      Parameters:
        account_name (str): the name of the account, case insensitive
      
      Returns:
        Account
    '''
    db_account = crud.get_account(db, name=account.name)
    if db_account:
        raise HTTPException(status_code=400, detail="Account already exists")
    return crud.create_account(db=db, account=account)


@router.get("/{account_name}", status_code=200)
def get_account(account_name: str, db: Session = Depends(get_db)):
    '''
    Gets an account with the given name (case insensitive)

      Parameters:
        account_name (str): the name of the account, case insensitive
      
      Returns:
        Account
    '''
    db_account = crud.get_account(db, name=account_name)
    if not db_account:
        return Response(status_code=404)
    return db_account


@router.post("/{account_name}/deposit", status_code=200)
def deposit(account_name: str, deposit: schema.DepositWithdraw, db: Session = Depends(get_db)):
    '''
    Deposits given amount into the given account name
    
      Parameters:
        account_name (str): the name of the account, case insensitive
        amount (float): the amount you want to deposit
      
      Returns:
        Account
    '''
    amount = get_amount(deposit.amount)
    db_account = crud.get_account(db, name=account_name)
    if not db_account:
        return Response(status_code=404)
    return crud.deposit(db=db, account=db_account, amount=amount)


@router.post("/{account_name}/withdraw", status_code=200)
def withdraw(account_name: str, withdraw: schema.DepositWithdraw, db: Session = Depends(get_db)):
    '''
    Withdraws given amount from the given account name

      Parameters:
        account_name (str): the name of the account, case insensitive
        amount (float): the amount you want to withdraw
      
      Returns:
        Account
    '''
    amount = get_amount(withdraw.amount)
    db_account = crud.get_account(db, name=account_name)
    if not db_account:
        return Response(status_code=404)
    if db_account.balance < amount:
        raise HTTPException(
            status_code=400, detail="Not enough funds")
    return crud.withdraw(db=db, account=db_account, amount=amount)

def get_amount(amount):
    amount = float(deposit.amount)
    actual_amount = float("{:.2f}".format(amount))
    if actual_amount != amount:
        raise HTTPException(
            status_code=400, detail="Please do not use more than 2 decimal places")
    return actual_amount
