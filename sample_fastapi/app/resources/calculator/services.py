class ConverterService:
    """Data conversion service"""
    def __init__(self):
        pass

    def dec2hex(self, value: int) -> str:
        """Convert integer to hexadecimal string with '0x' prefix"""
        return hex(value)

    def hex2dec(self, value: str) -> int:
        """Convert hexadecimal string (with or without prefix) into integer.

        Raises `ValueError` for incorrect input"""
        return int(value, 16)
