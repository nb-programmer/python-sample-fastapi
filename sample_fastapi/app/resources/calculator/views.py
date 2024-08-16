from fastapi import Depends, HTTPException, status

from .models import ConversionDecResponse, ConversionHexResponse
from .services import ConverterService


async def conv_dec2hex(value: int, converter: ConverterService = Depends(ConverterService)) -> ConversionHexResponse:
    """Convert integer input into hexadecimal string"""
    return ConversionHexResponse(
        value=converter.dec2hex(value),
    )


async def conv_hex2dec(value: str, converter: ConverterService = Depends(ConverterService)) -> ConversionDecResponse:
    """Convert hexadecimal string input into integer"""
    try:
        return ConversionDecResponse(
            value=converter.hex2dec(value),
        )
    except ValueError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Invalid hexadecimal input "%s"' % value,
        )
