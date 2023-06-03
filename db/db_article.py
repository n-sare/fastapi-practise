from db.hash import Hash
from db.models import DbArticle
from schemas import ArticleBase
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from exceptions import StoryException

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('Once upon a time'):
        raise StoryException('No stories please')
    new_article = DbArticle(
        title= request.title,
        content= request.content,
        published= request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    #sends new article to database
    db.commit()
    # database itself creates an id for new article, to get that we need to refresh
    db.refresh(new_article)
    return new_article

def get_all_articles(db: Session):
    return db.query(DbArticle).all()

def get_article(db: Session, id: int):
    article= db.query(DbArticle).filter(DbArticle.id==id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Article with id {id} not found')
    return article

def update_article(db: Session, id: int, request: ArticleBase):
    article = db.query(DbArticle).filter(DbArticle.id==id)
    article.update({
        DbArticle.title: request.title,
        DbArticle.content: request.content,
        DbArticle.published: request.published
    })
    db.commit()
    return 'ok'

def delete_article(db: Session, id: int):
    article= db.query(DbArticle).filter(DbArticle.id == id).first()
    db.delete(article)
    db.commit()
    return 'ok'