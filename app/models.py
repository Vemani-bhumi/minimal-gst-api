
from email.policy import default
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True,nullable=False)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    role = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))  



class TaxDue(Base):
    __tablename__ = "taxdue" 
    id = Column(Integer, primary_key=True,nullable=False) 
    user_id = Column(Integer,ForeignKey("users.user_id",ondelete="CASCADE"),primary_key=True,nullable=False)
    pan_card = Column(String,nullable=False)
    income_salary = Column(Integer, nullable=False)
    income_stock = Column(Integer, nullable=False) 
    state_code = Column(String,nullable=False)
    fines = Column(Integer,nullable=False)
    cgst = Column(Integer,nullable=False)
    sgst = Column(Integer,nullable=False) 
    status = Column(String,nullable=False,default="new")

