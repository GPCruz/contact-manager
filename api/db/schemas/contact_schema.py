from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

class ContactBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    contact_type: str
    call_type: Optional[str] = None
    call_frequency: Optional[timedelta] = None
    notes: Optional[str] = None
    last_call_date: Optional[datetime] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True