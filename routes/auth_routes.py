from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import usersignup, userlogin
from dependencies import get_current_user
from services.auth_service import user_signup, user_login, userrefresh_token, user_logout



router=APIRouter()

@router.post("/signup")
def signup(user:usersignup):
    return user_signup(user)


@router.post("/login")
def login(user:userlogin):
    token=user_login(user)
    
    response=JSONResponse(
        content={
            "message":"Login successful",
            "access_token": token["access_token"],
            "refresh_token": token["refresh_token"]
        }
    )
    
    response.set_cookie(
        key="access_token",
        value=token["access_token"],
        httponly=True
    )
    
    response.set_cookie(
        key="refresh_token",
        value=token["refresh_token"],
        httponly=True
    )
    
    return response


@router.get("/dashboard")
def dashboard(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }

@router.post("/refresh")
def refresh(request:Request):
    result=userrefresh_token(request)
    
    response=JSONResponse(
        content="token refresh"
    )
    
    response.set_cookie(
    key="access_token",
    value=result,
    httponly=True,
    max_age=1800
    )
    
    return response
    
    
@router.post("/logout")
def logout(request:Request):
    
    refresh_token = request.cookies.get(
        "refresh_token"
    )

    user_logout(
        refresh_token
    )
    
    response=JSONResponse(
        content={
            "message":"logout successfully"
        }
    )
    
    response.delete_cookie(
        key="access_token"
        
    )
    
    response.delete_cookie(
        key="refresh_token"
        
    )

    return response
    
    
    