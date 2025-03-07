from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "Imagine a post here"}

@app.post("/createposts")
async def create_posts():
    return {"message": "Successfully created post."}