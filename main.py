from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel #we can define a schema using this library

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #we can assign a default value
    rating : Optional[int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "Imagine a post here"}

@app.post("/createposts")
def create_posts(new_post: Post): #post class instance assigned to variable post
    print(new_post.published) #new_post.title will access the string value
    return {"data": "new_post"}
