"""Various utility functions"""


def str_quote(s: str, quote_char: str = '"') -> str:
    """Add quote characters surrounding the given string"""
    return f"{quote_char}{s}{quote_char}"
