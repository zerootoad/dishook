from typing import Optional, Dict, List, Any, Union
from datetime import datetime

class DiscordPoll:
    """
    A class for creating Discord polls.
    """

    def __init__(self, question: str, options: List[str]) -> None:
        """
        Initialize a Discord poll method.

        Parameters:
            question (str): The poll question.
            options (List[str]): List of poll options.
        """
        self.question = question
        self.options = options

    def set_question(self, question: str) -> None:
        """
        Set the question of the poll.

        Parameters:
            question (str): The poll question.
        """
        self.question = question

    def add_option(self, option: str) -> None:
        """
        Add an option to the poll.

        Parameters:
            option (str): Option to add to the poll.
        """
        self.options.append(option)

    def remove_option(self, index: int) -> None:
        """
        Remove an option from the poll by index.

        Parameters:
            index (int): Index of the option to remove.
        """
        if 0 <= index < len(self.options):
            self.options.pop(index)
        else:
            raise IndexError("Option index out of range.")

    def get_options(self) -> List[str]:
        """
        Get all options of the poll.

        Returns:
            List[str]: List of all options in the poll.
        """
        return self.options

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the poll object to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the poll.
        """
        return {
            "question": self.question,
            "options": self.options
        }
