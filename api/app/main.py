from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import Base, engine, get_db
from app.routes.user_routes import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="SolidKey API", version="0.1.0", lifespan=lifespan)
app.include_router(user_router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    "Verifies db connection"
    result = db.execute(text("SELECT 1")).scalar()
    return {"database": "connected" if result == 1 else "error"}
