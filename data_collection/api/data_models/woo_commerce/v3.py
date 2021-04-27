from typing import List, Dict
from datetime import datetime
from pydantic import BaseModel


class Shipping(BaseModel):
    first_name: str
    last_name: str
    company: str
    address_1: str
    address_2: str
    city: str
    state: str
    postcode: int
    country: str


class Billing(Shipping):
    email: str
    phone: str


class CustomerResponse(BaseModel):
    id: str
    date_created: datetime
    date_created_gmt: datetime
    email: str
    first_name: str
    last_name: str
    role: str
    username: str
    billing: Billing
    shipping: Shipping
    is_paying_customer: bool
    avatar_url: str
    meta_data: List
    _links: Dict[str, List[Dict[str, str]]]


class CustomerError(BaseModel):
    class Data(BaseModel):
        status = int
    code: str
    message: str
    data: Data
