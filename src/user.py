"""Provides a class to represent a user in the system."""


class User:
    """A class to represent a user in the system."""

    def __init__(self, user_id: int, name: str, balance: float, withdraw_times: int) -> None:
        self.id = user_id
        self.name = name
        self.balance = balance
        self.withdraw_times = withdraw_times

    def deposit(self, amount: float) -> None:
        """Deposits money into the user's account.

        Args:
            amount (float): The amount to deposit.
        """

        print(f'Depositando {amount}...')

    def withdraw(self, amount: float) -> None:
        """Withdraws money from the user's account.

        Args:
            amount (float): The amount to withdraw.
        """

        print(f'Sacando {amount}...')

    def get_statement(self):
        """Returns the user's statement."""

        print('Exibindo extrato...')
