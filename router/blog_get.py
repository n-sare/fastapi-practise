from fastapi import status, Response, APIRouter, Depends
from enum import Enum
from typing import Optional

from router.blog_post import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

#order matters, if you inter-change get_all_blog and get_blog methods /blog/all will throw an error bc 
# first method excepts int as id and 'all is string
@router.get('/all', summary='Retrieve all blogs', response_description='The list of available blogs')
def get_all_blog():
    '''
    This is a description you can see on swagger
    '''
    return {'message': 'All blogs provided'}

#this is query parameter, if it's in url it is called path parameter
@router.get('/allposts', description='This is another way to define description')
def get_all_blog_posts(page = 1, page_size: Optional[int]=None, req_parameter: dict = Depends(required_functionality) ):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool= True, username: Optional[str]= None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short='short'
    story='story'
    howto='howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id> 5:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with {id} not found'}
    else: 
        response.status_code= status.HTTP_200_OK
        return {'message': f'Blog with {id}'}
