from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root(): 
    return {"message": "hi"}

@app.get("/articles", response_model=list[schemas.ArticleOut])
def list_articles(tag: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Article)
    if tag:
        query = query.filter(models.Article.tags.contains(tag))
    return query.all()


@app.get("/articles/{article_id}", response_model=schemas.ArticleOut)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.get(models.Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.post("/articles", response_model=schemas.ArticleOut, status_code=201)
def create_article(data: schemas.ArticleIn, db: Session = Depends(get_db)):
    article = models.Article(**data.model_dump())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@app.put("/articles/{article_id}", response_model=schemas.ArticleOut)
def update_article(article_id: int, data: schemas.ArticleIn, db: Session = Depends(get_db)):
    article = db.get(models.Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    article.title = data.title
    article.content = data.content
    article.tags = data.tags
    db.commit()
    db.refresh(article)
    return article


@app.delete("/articles/{article_id}", status_code=204)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.get(models.Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(article)
    db.commit()