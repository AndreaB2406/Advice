from pydantic import BaseModel, Field, validator
from typing import Optional

class Filter(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None

class Pagination(BaseModel):
    page: Optional[int]
    @validator('page')
    def page_check(cls, page):
        if page is not None:
            if page<1:
                raise ValueError('page must be an integer greater than or equal to 1')
            else:
                return page

    per_page: Optional[int]
    @validator('per_page')
    def per_page_check(cls, per_page):
        if per_page is not None:
            if per_page<1:
                raise ValueError('per_page must be an integer greater than or equal to 1')
            else:
                return per_page

class InputData(BaseModel):
    id_catalog: int = Field()
    @validator('id_catalog')
    def id_catalog_check(cls, id_catalog):
        if id_catalog<1 or id_catalog>9:
            raise ValueError('id_catalog must be an integer between 1 and 9')
        else:
            return int(id_catalog)
    filter: Optional[Filter]
    pagination: Optional[Pagination]