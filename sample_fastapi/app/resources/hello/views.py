from fastapi import Query

from .models import HelloMessage


async def respond_hello() -> HelloMessage:
    """Respond with "Hello, World!" message in a JSON"""
    return HelloMessage(message="Hello, World!")


async def respond_name_greet(name: str = Query()) -> HelloMessage:
    """Respond with "Hello, <name>!" message in a JSON"""
    return HelloMessage(message=f"Hello, {name}!")
