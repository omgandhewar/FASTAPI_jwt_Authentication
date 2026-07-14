from pydantic import BaseModel


class usersignup(BaseModel):
    name:str
    email:str
    password:str
    
    
class userlogin(BaseModel):
    email:str
    password:str
    
