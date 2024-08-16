class ConverterService:
    def __init__(self):
        pass

    def dec2hex(self, value: int) -> str:
        return hex(value)

    def hex2dec(self, value: str) -> int:
        return int(value, 16)
