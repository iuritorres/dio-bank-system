"""Provides a decorator to connect to the database."""


from enum import StrEnum
from sqlite3 import OperationalError, connect

from utils import TerminalColors, Utils

DATABASE_PATH = 'src\\repositories\\database.db'


class StatementTypes(StrEnum):
    """Enumeration of statement types."""

    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'


def db_connect(func):
    """Provides a decorator to connect to the database."""

    def _db_connect(*args, **kwargs):
        connection = connect(DATABASE_PATH)
        cursor = connection.cursor()

        try:
            result = func(cursor, *args, **kwargs)
        except OperationalError as error:
            message = Utils.colorize('Error: ', TerminalColors.RED)
            print(message, error)

        connection.commit()
        connection.close()
        return result

    return _db_connect
