from fastapi import FastAPI
from db.database import engine
from models import User
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router




app=FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

app.include_router(router)




User.metadata.create_all(bind=engine)