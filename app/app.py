from fastapi import FastAPI, File,HTTPException, UploadFile, Form, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield



app = FastAPI(lifespan=lifespan)
@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)

): 
    post = Post(
        caption=caption,
        url="dummyurl",
        file_type="photo",
        file_name="dummy name"
        )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
    ):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data=[]
    for post in posts:
        posts_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })
    return {"posts": posts_data}










""""
text_posts = {
    1: {"title": "First Post", "content": "cool test post"},
    2: {"title": "Second Post", "content": "another test post"},
    3: {"title": "Third Post", "content": "this is post number three"},
    4: {"title": "Fourth Post", "content": "content for post four"},
    5: {"title": "Fifth Post", "content": "post five is here"},
    6: {"title": "Sixth Post", "content": "testing post six"},
    7: {"title": "Seventh Post", "content": "lucky number seven"},
    8: {"title": "Eighth Post", "content": "post eight content"},
    9: {"title": "Ninth Post", "content": "almost last one"},
    10: {"title": "Tenth Post", "content": "this is the final post"},
}
@app.get("/posts")
def get_all_posts(Limit: int = None):
    if Limit:
        return list(text_posts.values())[:Limit]
    return text_posts   

@app.get("/posts/{id}")
def get_post(id:int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content  }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
"""