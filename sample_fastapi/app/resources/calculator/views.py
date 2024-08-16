from fastapi import Depends, HTTPException, status

from .models import ConversioDecResponse, ConversioHexResponse
from .services import ConverterService


async def calc_dec2hex(value: int, converter: ConverterService = Depends(ConverterService)) -> ConversioHexResponse:
    return ConversioHexResponse(
        value=converter.dec2hex(value),
    )


async def calc_hex2dec(value: str, converter: ConverterService = Depends(ConverterService)) -> ConversioDecResponse:
    try:
        return ConversioDecResponse(
            value=converter.hex2dec(value),
        )
    except ValueError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Invalid hexadecimal input "%s"' % value,
        )
