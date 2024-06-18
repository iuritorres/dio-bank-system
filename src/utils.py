"""Provides utilities classes"""


from enum import StrEnum


class TerminalColors(StrEnum):
    """A Set of python suported terminal colors"""

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


class Utils:
    """A class that provides utility functions"""

    @staticmethod
    def colorize(text: str, color: TerminalColors) -> str:
        """Colorize the text with the given color"""
        return f'{color.value}{text}{TerminalColors.RESET.value}'
