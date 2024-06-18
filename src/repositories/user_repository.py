"""Provides a class to represent a userRepository in the system."""


from .database import db_connect


class UserRepository:
    """Provides a class to represent a userRepository in the system."""

    @staticmethod
    def initialize() -> None:
        """Initializes the userRepository."""

        UserRepository.drop_table()
        UserRepository.create_table()
        UserRepository.populate_table()

    @staticmethod
    @db_connect
    def drop_table(cursor=None) -> None:
        """Drops the user table in the database."""

        cursor.execute('DROP TABLE IF EXISTS users;')

    @staticmethod
    @db_connect
    def create_table(cursor=None) -> None:
        """Creates the user table in the database."""

        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                withdraw_times INTEGER DEFAULT 0 NOT NULL
            );
        ''')

    @staticmethod
    @db_connect
    def populate_table(cursor=None) -> None:
        """Populates the user table in the database."""

        cursor.execute('''
            INSERT INTO users (name, balance) VALUES
            ('Bob Dylan', 2000.0),
            ('Iuri Barbosa Torres', 1200.0),
            ('Charlie Puth', 3000.0),
            ('David Bowie', 4000.0),
            ('Bonnie Tyler', 5000.0);
        ''')

    @staticmethod
    @db_connect
    def get_by_id(cursor=None, user_id: int = None) -> tuple:
        """Retrieves a user by their ID."""

        cursor.execute('SELECT * FROM users WHERE id = ?;', (user_id,))
        return cursor.fetchone()
