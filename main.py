from fastapi import FastAPI
from db.database import engine
from models import User
from routes.auth_routes import router




app=FastAPI()


app.include_router(router)



User.metadata.create_all(bind=engine)