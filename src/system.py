"""Provides a class to represent the system."""

from os import system as os_system
from random import randint

from pynput.keyboard import Key, KeyCode, Listener

from input_handler import InputHandler
from repositories import StatementRepository, UserRepository
from user import User
from utils import TerminalColors, Utils


class System:
    """Provides a class to represent the system."""

    __WITHDRAW_LIMIT = 3
    __WITHDRAW_MAX_VALUE = 500
    __COLOR = TerminalColors.CYAN
    __COLOR_LENGTH = len(__COLOR.value) + len(TerminalColors.RESET.value)

    def __init__(self, user_id: int = None) -> None:
        self.current_user: User = None
        self.keyboard_listener: Listener = None

        self.__initialize_repositories()
        self.login(user_id)

        self.options = [
            {
                "name": "Depósito",
                "is_selected": True,
                "action": self.current_user.deposit,
            },
            {
                "name": "Saque",
                "is_selected": False,
                "action": self.current_user.withdraw,
            },
            {
                "name": "Extrato",
                "is_selected": False,
                "action": self.current_user.get_statement,
            },
        ]

    def initialize(self) -> None:
        """Initializes the system."""

        # os_system("cls")
        self.menu()

    def menu(self) -> None:
        """Displays the menu."""
        self.__show_options()

        self.keyboard_listener = self.__create_listener()
        self.keyboard_listener.join()

    def __show_options(self) -> None:
        """Shows the options."""

        title = Utils.colorize("DIO Bank", self.__COLOR)
        title_bar = f"=============  <<< {title} >>>  ============="
        title_bar_length = len(title_bar) - self.__COLOR_LENGTH

        empty_space = f'‖{" " * (title_bar_length - 2)}‖'

        print(title_bar)
        print(empty_space)

        for option in self.options:
            option_name = Utils.colorize(option.get("name"), self.__COLOR)

            right_padding = title_bar_length - len(option_name) + 3
            select = "▶" if option.get("is_selected") else " "

            print(f'{"‖"}  {select} {option_name} { "‖".rjust(right_padding)}')

        print(empty_space)
        print(
            f'{"‖".ljust(4)} {"Pressione ESC para sair."} {"‖".rjust(len(empty_space) - 30)}'
        )
        print(empty_space)

        print("=" * title_bar_length)

    def __unselect_option(self, index: int) -> None:
        """Unsets the current option.

        Args:
            index (int): The index of the option to unselect.
        """

        self.options[index]["is_selected"] = False

    def __get_current_option_index(self) -> int:
        """Returns the current option index."""

        return next(
            filter(lambda option: option[1].get("is_selected"), enumerate(self.options))
        )[0]

    def __on_press(self, key: str | Key | KeyCode) -> None:
        current_index = self.__get_current_option_index()

        match key:
            case Key.up:
                self.__unselect_option(current_index)

                if current_index == 0:
                    self.options[len(self.options) - 1]["is_selected"] = True
                else:
                    self.options[current_index - 1]["is_selected"] = True

            case Key.down:
                self.__unselect_option(current_index)

                if current_index == len(self.options) - 1:
                    self.options[0]["is_selected"] = True
                else:
                    self.options[current_index + 1]["is_selected"] = True

            case Key.enter:
                self.keyboard_listener.stop()

                action = self.options[current_index]["action"]

                if "amount" in action.__code__.co_varnames:
                    amount = InputHandler.get_float()
                    action(amount)

                    self.__show_options()
                else:
                    action()

                self.keyboard_listener = self.__create_listener()
                self.keyboard_listener.join()

            case Key.esc:
                self.__show_quit_message()
                return False

        # os_system("cls")
        self.__show_options()

    def __create_listener(self) -> Listener:
        """Creates a listener.

        Returns:
            Listener: A pynput listener instance.
        """

        listener = Listener(on_press=self.__on_press)
        listener.start()
        return listener

    def __initialize_repositories(self) -> None:
        """Initializes the repositories."""

        UserRepository.initialize()
        StatementRepository.initialize()

    def login(self, user_id: int) -> None:
        """Logs the user in.

        Args:
            user_id (int): The user ID.
        """

        user = UserRepository.get_by_id(user_id)

        if user:
            self.current_user = User(
                user_id=user[0], name=user[1], balance=user[2], withdraw_times=user[3]
            )
        else:
            message = Utils.colorize("[LOGIN] User not found.", TerminalColors.RED)
            print(message)

    def __show_quit_message(self) -> None:
        """Quits the system."""

        message = Utils.colorize(
            "=========  <<< Até a Próxima >>>  =========", TerminalColors.GREEN
        )

        os_system("cls")
        print("\n" * 2)
        print(message, end="\n" * 4)
