from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict
router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key' : 'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int= 1):
    return {
        'id': id,
        'data': blog,
        'version': version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
        comment_title: str= Query(None,
        title='Id of the comment',
        description= 'Description for comment_title',
        alias='commentTitle',
        deprecated=True),
        #optional default valued parameter
        content: str = Body('hi how you doin'),
        #mandatory parameter
        mandatory: str = Body(..., min_length=10, max_length=15),
        v: Optional[List[str]] = Query(['1.0', '1.1', '1.2', '1.3']),
        comment_id: int = Path(..., gt=5, le=10)
        
    ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'mandatory': mandatory,
        'comment_id': comment_id,
        'version': v

    }

def required_functionality():
    return {'message': 'Learning FastAPI is important'}