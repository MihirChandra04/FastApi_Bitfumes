from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from . import token,database,models
from sqlalchemy.orm import session

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme),
    db: session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    ) 
    
    token_data = token.verify_token(data, credentials_exception)

    user = db.query(models.User).filter(models.User.email == token_data.email).first() 
    if user is None:
        raise credentials_exception

    return user