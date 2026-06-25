from fastapi import FastAPI, Request, HTTPException
from db.database import sessionlocal
from jose import jwt, JWTError
from utils.jwt import SECRET_KEY, ALGORITHM
from models import User, token
from utils.password import hashed_password, verify_password
from utils.jwt import create_access_token, create_refresh_token


def user_signup(user):
    db=sessionlocal()
    
    
    name=user.name
    email=user.email
    password=user.password
    
    user_obj=db.query(User).filter(User.email==email).first()
    
    if user_obj:
        return{
            "message":"user alsready exixts"
        }
        
    print(password)
    print(type(password))
    print(len(password))    
        
    hashed_password1=hashed_password(password)
        
    user=User(
        name=name,
        email=email,
        password=hashed_password1
    )
    
    db.add(user)
    db.commit()
    
    return{
        "message":"user added successfully"
    }
    
    
def user_login(user):
    db=sessionlocal()
    
    email=user.email
    password=user.password
    
    if not email or not password:
        raise HTTPException(
        status_code=400,
        detail="email and password are required"
    )
    
    user_obj=db.query(User).filter(User.email==email).first()
    
    
    if not user_obj:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    
    is_valid = verify_password(
        user.password,
        user_obj.password
    )
    
    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
        
    access_token=create_access_token({
        "user_id":user_obj.id
    })
    
    refresh_token=create_refresh_token({
        "user_id":user_obj.id
    })
    
    return{
        "access_token":access_token,
        "refresh_token":refresh_token
    }


def userrefresh_token(request:Request):  
    db=sessionlocal()
    
    refresh_token=request.cookies.get("refresh_token")
    
    if not refresh_token:
        raise HTTPException(status_code=401,detail="refresh token is missing")
    
    
    try:
        payload=jwt.decode(
            refresh_token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )
        
    except JWTError:
        raise HTTPException(status_code=401,detail="invalid refresh token")
    
    
    user_id=payload.get("user_id")
    
    jti=payload.get("jti")
    
    
    jti=db.query(token).filter(token.jti==jti).first()
    
    if jti:
        raise HTTPException(
        status_code=401,
        detail="Token revoked"
        )   
    
    new_access_token=create_access_token({
        "user_id":user_id
    })
    
    return new_access_token


def user_logout(refresh_token):
    db=sessionlocal()
    
    
    payload=jwt.decode(
        refresh_token,
        SECRET_KEY,
        algorithms=ALGORITHM
    )
    
    jti=payload.get("jti")
    
    user=token(
        jti=jti,
        refresh_token=refresh_token
    )
    
    db.add(user)
    db.commit()
    
    return refresh_token
    