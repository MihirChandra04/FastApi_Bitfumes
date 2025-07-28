from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,token
from sqlalchemy.orm import session
from ..hashing import Hash
from fastapi.security import  OAuth2PasswordRequestForm


router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends() , db:session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"username {request.username} is not found")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")
    
    #generate JWT token--python-jose
    access_token = token.create_access_token(
        data={"sub": request.username}
    )
    return {"access_token":access_token, "token_type":"bearer"}