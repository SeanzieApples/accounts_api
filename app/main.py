#!/usr/bin/env python3
from fastapi import FastAPI
from .routers import account
from .db.database import Base, engine

app = FastAPI(title="Accounts API")
app.include_router(account.router)

Base.metadata.create_all(engine)