from pydantic import BaseModel


class ConversioHexResponse(BaseModel):
    value: str


class ConversioDecResponse(BaseModel):
    value: int
