from pydantic import BaseModel, EmailStr, constr
from typing import Literal

class RegistrationData(BaseModel):
    name: constr(min_length=1)
    email: EmailStr
    phone: constr(min_length=6)
    age: int
    sex: Literal['чоловіча', 'жіноча']
    password: constr(min_length=8)
