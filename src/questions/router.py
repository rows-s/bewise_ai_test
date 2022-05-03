from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.orm.session import Session

from .cru_models import Read

__all__ = ['router']


router = APIRouter(tags=['questions'])


@cbv(router)
class Questions:
    session: Session = Depends(...)

    @router.get('/')
    def read(self, body=Read):
        pass




