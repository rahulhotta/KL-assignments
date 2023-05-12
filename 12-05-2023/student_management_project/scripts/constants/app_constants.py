from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    age: int
    branch: str

class Email(BaseModel):
    rec_email: str
    subject: str
    body: str