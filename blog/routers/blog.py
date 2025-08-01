from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import schemas,database,oauth2
from typing import List
from ..repository import blog



router= APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)


get_db=database.get_db


@router.get('/',response_model=List[schemas.showBlog])
def all(db: Session= Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog , db: Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db,current_user)


@router.get('/{id}',status_code=200,response_model=schemas.showBlog)
def show(id, db: Session= Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session =Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
 


#we need request body for put and create method
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)