from fastapi import APIRouter,Depends
from .. import schemas,database
from sqlalchemy.orm import Session
from ..repository import user


get_db=database.get_db

router=APIRouter(
    tags=['Users'],
    prefix="/user"
)


@router.post('/',response_model=schemas.showUser)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    return user.create_user(request,db)
    


@router.get('/{id}',response_model=schemas.showUser)
def get_user(id, db:Session = Depends(get_db)):
    return user.show(id,db)