from pydantic import BaseModel
from datetime import datetime
class Guestbook(BaseModel):
    id: int
    name: str
    comments: str
    createdAt: datetime

