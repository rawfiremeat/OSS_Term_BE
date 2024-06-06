from fastapi import FastAPI, Path
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from DTO import Guestbook
from datetime import datetime
app = FastAPI()

comments_list = []

origins = [
    "http://127.0.0.1:5500", "http://3.213.20.133"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def welcome() -> str:
    return "test"
    

@app.get("/comments")
async def get_comments() -> dict:
    return {
        "comments": comments_list
    }
@app.get("/comments/{comments_id}")
async def get_comments_by_id(comments_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for comment in comments_list:
        if comment.id == comments_id:
            return {
                "comment": comment
            }
    return { "status": 400,
            "msg": "그런 아이디는 없어요"}

@app.post("/comments")
async def post_comment(comment: Guestbook) -> dict:
    comment.id = len(comments_list) + 1
    comment.createdAt = datetime.utcnow()
    comments_list.append(comment)
    return {
        "status" : 200,
        "msg" : "added successfully"
    } 

@app.delete("/comments/{comments_id}")
async def delete_comment(comments_id:int = Path(..., title = "the ID of the todo to delete")):
    for index, comment in enumerate(comments_list):
        if comment.id == comments_id:
            del comments_list[index]
        return {"msg": f"{comments_id} comment deleted successfully"}
    return {"msg" : "supplied ID doesn't exist"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)