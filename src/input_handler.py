"""
This module handles input for the bank system.

It provides functions to validate and process user input.
"""


class InputHandler:
    """A class to handle input for the bank system."""

    @staticmethod
    def get_float() -> float:
        """Get by input and validates the amount entered by the user.

        Returns:
            float: The amount entered by the user.
        """

        while True:
            amount = input("Digite o valor: ")

            try:
                amount = float(amount)
            except ValueError:
                print("Valor inválido. Por favor, tente novamente.")
                continue

            if amount <= 0:
                print("O valor deve ser maior que zero.")
                continue

            return amount
