import shutil
from dataclasses import dataclass


@dataclass
class Menu:
    """
    A class representing a main menu with options.
    """

    menu_text: list

    def display_menu_border(self, padding):
        """
        Display the border of the main menu.
        """
        border = "╔" + "═" * (len(max(self.menu_text, key=len)) + 2) + "╗"
        print(" " * padding + border)

    def display_option(self, option, padding):
        """
        Display a menu option with ASCII formatting.
        """
        print(" " * padding + f"║ {option:<15} ║")

    def display_menu_footer(self, padding):
        """
        Display the footer of the main menu.
        """
        footer = "╚" + "═" * (len(max(self.menu_text, key=len)) + 2) + "╝"
        print(" "*padding + footer)

    def display(self):
        """
        Display the main menu with ASCII graphics.
        """
        # Get the terminal size
        terminal_width, _ = shutil.get_terminal_size()

        # Calculate padding to center the text
        max_length = max(len(line) for line in self.menu_text)
        padding = (terminal_width - max_length) // 2

        self.display_menu_border(padding)
        for line in self.menu_text:
            centered_line = line.center(max_length)
            self.display_option(centered_line, padding)
        self.display_menu_footer(padding)

    def center_text(self, text, width):
        """
        Center the given text within a specified width.
        """
        padding = (width - len(text)) // 2
        return " " * padding + text

    def run(self) -> int:
        """
        Run the main menu and handle user input.
        """
        self.display()
        print("\n")
        choice = int(input(self.center_text(
            "[*] Escolha uma opção: ", shutil.get_terminal_size().columns))
        )
        return choice
