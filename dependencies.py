from fastapi import FastAPI, Request, HTTPException
from  db.database import sessionlocal
from models import User
from jose import jwt, JWTError
from utils.jwt import SECRET_KEY, ALGORITHM



def get_current_user(request:Request):
    
    token=request.cookies.get("access_token")
    
    if not token:
        raise HTTPException(status_code=401,detail="Not Authenticated")
    
    try:
        
       payload=jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
       )
    
       user_id=payload.get("user_id")
     
       if user_id is None:
           raise HTTPException(
                status_code=401,
                detail="Invalid Token"
               )
           
    except JWTError:
        
         raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    db = sessionlocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
          
    