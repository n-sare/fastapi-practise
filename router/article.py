from typing import List
from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay, UserBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import get_current_user, oauth2_scheme


router = APIRouter(
    prefix='/article',
    tags=['article']
)

#create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)

#read all articles
@router.get('/', response_model=List[ArticleDisplay])
def get_all_articles(db: Session=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.get_all_articles(db)

#read one article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.get_article(db, id)


#update user
@router.post('/{id}/update')
def update_article(id: int, request: ArticleBase, db: Session= Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.update_article(db, id, request)

#delete user
@router.get('/delete/{id}')
def delete_article(id: int, db: Session=Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.delete_article(db, id)