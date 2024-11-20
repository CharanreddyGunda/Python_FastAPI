from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List,Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class UserBase(BaseModel):
    first_name: str
    last_name:str
    gender: str
    age: int
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/api/user/register")
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(first_name=user.first_name, last_name=user.last_name, gender=user.gender, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)