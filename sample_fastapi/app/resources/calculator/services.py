class ConverterService:
    """Data conversion service"""
    def __init__(self):
        pass

    def dec2hex(self, value: int) -> str:
        """Convert integer to hexadecimal string with '0x' prefix.

        :param int value: Integer value to convert (can be negative, zero and positive)
        :return str: The converted hexadecimal with '0x' prefix
        """
        return hex(value)

    def hex2dec(self, value: str) -> int:
        """Convert hexadecimal string (with or without prefix) into integer.

        :param str value: Hexadecimal value to convert
        :return int: The converted integer if `value` is a valid hexadecimal string
        :raises ValueError: Raised for incorrect input"""
        return int(value, 16)
