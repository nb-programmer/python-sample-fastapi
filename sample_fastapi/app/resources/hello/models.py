from pydantic import BaseModel


class HelloMessage(BaseModel):
    message: str
