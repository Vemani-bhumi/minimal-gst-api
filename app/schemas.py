from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username : str
    password : str
    role : str

class User(BaseModel):
    user_id : int
    username : str
    role : str
    class Config:
        orm_mode = True

class TaxDueCreate(BaseModel):
    user_id : int
    pan_card : str
    income_salary : int
    income_stock : int
    state_code : str
    fines : int
    cgst : int
    sgst : int

class TaxDue(BaseModel):
    id : int
    user_id : int
    pan_card : str
    income_salary : int
    income_stock : int
    state_code : str
    fines : int
    cgst : int
    sgst : int
    status : str
    class Config:
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    user_id : Optional[str] = None
    role : Optional[str] = None
    


    