from pydantic import BaseModel


class Member(BaseModel):
    name: str
    email: str
    state: str
    lga: str
    ward: str
    state_code: str

  
