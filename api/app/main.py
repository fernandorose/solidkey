from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from api.app.config.database import get_db

app = FastAPI(title="SolidKey API", version="0.1.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    """Verifica que la API puede hablar con Postgres."""
    result = db.execute(text("SELECT 1")).scalar()
    return {"database": "connected" if result == 1 else "error"}