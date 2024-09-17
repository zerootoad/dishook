from typing import Optional, Dict, List, Any, Union
from datetime import datetime

class DiscordUtilities:
    """
    A class for various Discord utility functions.
    """

    def create_timestamp(self, format: str) -> str:
        """
        Create a Discord timestamp in a specified format.

        Parameters:
            format (str): The format for the timestamp. Valid options are:
                - "R": Relative time.
                - "D": Long date.
                - "d": Short date.
                - "T": Long time.
                - "t": Short time.
                - "F": Long date/time.
                - "f": Short date/time.

        Returns:
            str: The formatted timestamp.

        Raises:
            ValueError: If an invalid format is provided.
        """
        valid_formats = {"R", "D", "d", "T", "t", "F", "f"}
        if format not in valid_formats:
            raise ValueError(f"Invalid format '{format}'. Must be one of {valid_formats}.")
        
        timestamp = int(datetime.now().timestamp())
        return f"<t:{timestamp}:{format}>"

    def convert_color_to_int(self, color: Union[str, int]) -> int:
        """
        Convert a color to an integer.

        Parameters:
            color (Union[str, int]): The color in hexadecimal (str) or decimal (int) format.

        Returns:
            int: The color in integer format.

        Raises:
            ValueError: If the color is out of the valid range.
        """
        if isinstance(color, str):
            color = int(color, 16)
        if not (0 <= color < 16777216):
            raise ValueError(f"Color {color} is out of the valid range.")
        return color