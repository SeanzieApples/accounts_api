#!/usr/bin/env python3
from fastapi import FastAPI
from .routers import account
from .db.database import Base, engine
from .base.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(account.router)

Base.metadata.create_all(engine)