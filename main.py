from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app=FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    # return published
    if published:
        return {'data': f'{limit}published blogs from the DB'}
    else:
        return {'data': f'{limit} blogs from the DB'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}



@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id=id 
    return {'data':id}



@app.get('/blog/{id}/comments')
def comments(id,limit):
    #here limit is query parameter(auto identified by fastapi) and id is path parameter
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title:str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return  {'data': f"Blog is created with title as {request.title}"}

#fro debugging
# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)