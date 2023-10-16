from starlette.background import BackgroundTasks
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from custom_log import log

from schemas import ProductBase

router = APIRouter(
    prefix='/templates',
    tags= ['templates']
)

templates = Jinja2Templates(directory='template')

@router.post('/products/{id}', response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call, f'Product with id {id}')
    return templates.TemplateResponse(
        'product.html',
        {
            'request': request,
            'id': id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        }
    )
#This is background task. It is called after the call is completed

def log_template_call(message: str):
    log('Message', message)