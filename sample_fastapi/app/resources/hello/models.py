from pydantic import BaseModel


class HelloMessage(BaseModel):
    """Message response to hello request"""
    message: str
