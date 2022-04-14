from fastapi import FastAPI
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models
from .routers import users,taxdue,auth
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host = "localhost", database = "gst", user="postgres", password="12345",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error:",error)
        time.sleep(2)

app.include_router(users.router)
app.include_router(taxdue.router)
app.include_router(auth.router)
 

@app.get("/")
def root():
    return {"message":"Welcome"} 