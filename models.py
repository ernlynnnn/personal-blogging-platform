from datetime import datetime, timezone

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base 

def utcnow(): 
    return datetime.now(timezone.utc)

class Article(Base): 
    __tablename__ = "articles" 

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text) 
    tags: Mapped[str] = mapped_column(String(200), default="")
    published_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow) 