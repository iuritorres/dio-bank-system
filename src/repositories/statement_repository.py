"""Provides a class to represent a statementRepository in the system."""


from .database import db_connect, StatementTypes


class StatementRepository:
    """Provides a class to represent a statementRepository in the system."""

    @staticmethod
    def initialize() -> None:
        """Initializes the statementRepository."""

        StatementRepository.drop_table()
        StatementRepository.create_table()

    @staticmethod
    @db_connect
    def drop_table(cursor=None) -> None:
        """Drops the statement table in the database."""

        cursor.execute('DROP TABLE IF EXISTS statements;')

    @staticmethod
    @db_connect
    def create_table(cursor=None) -> None:
        """Creates the statements table in the database."""

        cursor.execute('''
            CREATE TABLE statements (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                type TEXT NOT NULL,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
            );
        ''')

    @staticmethod
    @db_connect
    def insert(
        cursor=None,
        user_id: int = None,
        amount: float = None,
        statement_type: StatementTypes = None
    ) -> None:
        """Inserts a statement into the database."""

        cursor.execute('''
            INSERT INTO statements (user_id, amount, type)
            VALUES (?, ?, ?);
        ''', (user_id, amount, statement_type.value))

    @staticmethod
    @db_connect
    def get_by_user_id(cursor=None, user_id: int = None) -> list:
        """Retrieves all statements by a user ID."""

        cursor.execute(
            'SELECT * FROM statements WHERE user_id = ?;', (user_id,))
        return cursor.fetchall()
