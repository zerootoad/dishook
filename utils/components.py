from typing import Optional, Dict, List, Any, Union
from datetime import datetime

class DiscordComponents:
    """
    A class for creating Discord message components.
    """

    def __init__(self) -> None:
        """
        Initialize a Discord Components method.
        """
        self.components = []

    def add_action_row(self, components: List[Dict[str, Any]]) -> None:
        """
        Add an action row with components to the message.

        Parameters:
            components (List[Dict[str, Any]]): List of components to add in the action row.
        """
        self.components.append({"type": 1, "components": components})

    def add_button(self, label: str, custom_id: str, style: int = 1, emoji: Optional[Dict[str, Any]] = None, url: Optional[str] = None, disabled: bool = False) -> None:
        """
        Add a button component to an action row.

        Parameters:
            label (str): Label text of the button.
            custom_id (str): Custom ID of the button.
            style (int): Style of the button (1 to 5). Default is 1.
            emoji (Optional[Dict[str, Any]]): Emoji object for the button.
            url (Optional[str]): URL to open when the button is clicked (optional).
            disabled (bool): Whether the button is disabled. Default is False.
        """
        button = {"type": 2, "label": label, "custom_id": custom_id, "style": style, "disabled": disabled}
        if emoji:
            button["emoji"] = emoji
        if url:
            button["url"] = url

        self.components.append(button)

    def add_select_menu(self, custom_id: str, options: List[Dict[str, Any]], placeholder: str, min_values: int = 1, max_values: int = 1, disabled: bool = False) -> None:
        """
        Add a select menu component to an action row.

        Parameters:
            custom_id (str): Custom ID of the select menu.
            options (List[Dict[str, Any]]): List of options for the select menu.
            placeholder (str): Placeholder text when no option is selected.
            min_values (int): Minimum number of selectable options. Default is 1.
            max_values (int): Maximum number of selectable options. Default is 1.
            disabled (bool): Whether the select menu is disabled. Default is False.
        """
        select_menu = {
            "type": 3,
            "custom_id": custom_id,
            "options": options,
            "placeholder": placeholder,
            "min_values": min_values,
            "max_values": max_values,
            "disabled": disabled
        }

        self.components.append(select_menu)

    def get_components(self) -> List[Dict[str, Any]]:
        """
        Get all components added.

        Returns:
            List[Dict[str, Any]]: List of all components added.
        """
        return self.components
