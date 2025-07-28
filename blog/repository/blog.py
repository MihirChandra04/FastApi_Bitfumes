from sqlalchemy.orm import session
from .. import models,schemas
from fastapi import HTTPException,status
from sqlalchemy.orm import joinedload

def get_all(db:session):
    blogs=db.query(models.Blog).options(joinedload(models.Blog.creator)).all()
    return blogs


def create(request:schemas.Blog , db:session , current_user):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=current_user.id )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    db.refresh(new_blog, attribute_names=['creator'])  # Ensure creator is loaded
    return new_blog

def destroy(id:int,db:session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return f'blogid {id} deleted succefully' 


def update(id:int,db:session,request):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog id {id} is not available')
    blog.update(request.dict())
    db.commit()
    return 'updated succefully' 

def show(id:int,db:session):
    blog=db.query(models.Blog).options(joinedload(models.Blog.creator)).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} is not available")
    return blog