from datetime import datetime

from pydantic import BaseModel, ConfigDict

# what api sends back
class ArticleOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    content: str
    tags: str
    published_at: datetime
    updated_at: datetime

# what api accept 
class ArticleIn(BaseModel):
    title: str
    content: str
    tags: str = ""