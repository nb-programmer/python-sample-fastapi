from fastapi import Query

from .models import HelloMessage


async def respond_hello() -> HelloMessage:
    return HelloMessage(message="Hello, World!")


async def respond_name_greet(name: str = Query()) -> HelloMessage:
    return HelloMessage(message=f"Hello, {name}!")
