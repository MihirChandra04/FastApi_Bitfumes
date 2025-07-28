
from .. import hashing,models,schemas
from sqlalchemy.orm import session
# from ..hashing import Hash
from fastapi import status,HTTPException

def create_user(request:schemas,db:session):
    new_user=models.User(name=request.name,password=hashing.Hash.bcrypt(request.password)
                         ,email=request.email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id:int,db:session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user id {id} not found')
    return user