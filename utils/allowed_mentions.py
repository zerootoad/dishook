from typing import Dict, Any, Optional, List, Union

class DiscordAllowedMentions:
    """
    A class for handling allowed mentions in Discord messages.
    """

    def __init__(self, parse: Optional[List[str]] = None, users: Optional[List[str]] = None,
                 roles: Optional[List[str]] = None, replied_user: Optional[bool] = None) -> None:
        """
        Initialize DiscordAllowedMentions.

        Parameters:
            parse (Optional[List[str]]): The allowed mention types ('roles', 'users', 'everyone').
            users (Optional[List[str]]): Specific users to mention.
            roles (Optional[List[str]]): Specific roles to mention.
            replied_user (Optional[bool]): Whether to mention the user being replied to.
        """
        self.parse = parse
        self.users = users
        self.roles = roles

    def set_parse(self, **kwargs: Optional[Union[bool, List[str]]]) -> None:
        """
        Set the allowed mention types using keyword arguments.

        Parameters:
            **kwargs: Arbitrary keyword arguments to set mention types.
                Accepted keys: 'roles', 'users', 'everyone', 'parse'.
                - roles (bool): True to enable role mentions.
                - users (bool): True to enable user mentions.
                - everyone (bool): True to enable everyone mentions.
                - parse (List[str]): List of specific mention types ('roles', 'users', 'everyone').
        """
        parse = kwargs.get("parse")
        if parse is not None:
            self.parse = parse
        else:
            self.parse = []
            if kwargs.get("roles"):
                self.parse.append('roles')
            if kwargs.get("users"):
                self.parse.append('users')
            if kwargs.get("everyone"):
                self.parse.append('everyone')

    def add_user(self, user_id: int) -> None:
        """
        Add a user to be mentioned.

        Parameters:
            user_id (int): The ID of the user to mention.
        """
        if not self.users:
            self.users = []
        self.users.append(str(user_id))

    def add_role(self, role_id: int) -> None:
        """
        Add a role to be mentioned.

        Parameters:
            role_id (int): The ID of the role to mention.
        """
        if not self.roles:
            self.roles = []
        self.roles.append(str(role_id))

    def to_dict(self) -> Dict[str, Union[bool, Dict[str, List[str]]]]:
        """
        Convert the allowed mentions object to a dictionary.

        Returns:
            Dict[str, Union[bool, Dict[str, List[str]]]]: Dictionary representation of allowed mentions.
        """
        mentions_dict: Dict[str, Union[bool, Dict[str, List[str]]]] = {}

        if self.parse:
            mentions_dict["parse"] = self.parse

        if self.users:
            mentions_dict["users"] = self.users[100:]

        if self.roles:
            mentions_dict["roles"] = self.roles[100:]

        return mentions_dict