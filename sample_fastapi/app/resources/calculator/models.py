from pydantic import BaseModel


class ConversionHexResponse(BaseModel):
    """Hexadecimal value response"""
    value: str


class ConversionDecResponse(BaseModel):
    """Integer value response"""
    value: int
