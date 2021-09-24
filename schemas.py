from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'username': 'jojo',
                'email': 'jojo@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='e51c0378d81d300da91ccef9e45af589c33e05eb42f287107952e39f0871e29c'


class LoginModel(BaseModel):
    username:str
    password:str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str]='PENDING'
    pizza_size: Optional[str]='SMALL'
    user_id: Optional[int]


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'quantity': 1,
                'pizza_size': 'SMALL'
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = 'PENDING'

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'order_status': 'PENDING'
            }
        }