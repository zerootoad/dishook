import requests
from typing import Dict, Any, Optional, List
from utils.embed import DiscordEmbed
from utils.components import DiscordComponents
from utils.poll import DiscordPoll
from utils.allowed_mentions import DiscordAllowedMentions

class DiscordWebhook:
    """
    A class to handle Discord webhook requests.
    """

    def __init__(self, url: str) -> None:
        """
        Initialize the DiscordWebhook method.

        Parameters:
            url (str): The webhook URL.
        """
        self.id, self.token = self._parse_webhook_url(url)
        
        self.webhook_url = f"https://discord.com/api/webhooks/{self.id}/{self.token}"
        self.headers = {
            "Content-Type": "application/json"
        }
        
        self.parse = []
        self.users = []

    def _parse_webhook_url(self, url: str):
        parts = url.split("/")
        return parts[-2], parts[-1]

    def _embed_to_dict(self, embed: DiscordEmbed) -> Dict[str, Any]:
        """
        Convert a DiscordEmbed object to a dictionary.

        Parameters:
            embed (DiscordEmbed): The DiscordEmbed object to convert.

        Returns:
            Dict[str, Any]: The embed as a dictionary.
        """
        embed_dict = embed.to_dict()
        self.validate_embed_fields(embed_dict.get('fields', []))
        return embed_dict

    def validate_embed_fields(self, fields: List[Dict[str, Any]]) -> None:
        """
        Validate the fields in an embed.

        Parameters:
            fields (List[Dict[str, Any]]): The list of field dictionaries.

        Raises:
            ValueError: If any field is missing required keys or has invalid values.
        """
        for field in fields:
            if "name" not in field or "value" not in field:
                raise ValueError("Each field must have 'name' and 'value' keys.")
            if not isinstance(field["name"], str) or not isinstance(field["value"], str):
                raise ValueError("The 'name' and 'value' of each field must be strings.")
            if "inline" in field and not isinstance(field["inline"], bool):
                raise ValueError("The 'inline' key, if present, must be a boolean.")

    def execute(self, content: Optional[str] = None, embeds: Optional[List[DiscordEmbed]] = None,
                components: Optional[DiscordComponents] = None, poll: Optional[DiscordPoll] = None,
                username: Optional[str] = None, avatar_url: Optional[str] = None, tts: Optional[bool] = False,
                allowed_mentions: Optional[DiscordAllowedMentions] = None, ) -> requests.Response:
        """
        Send a message to the webhook.

        Key:
            * Requires an application-owned webhook.

        Parameters:
            content (Optional[str]): The message content.
            embeds (Optional[List[DiscordEmbed]]): A list of DiscordEmbed objects to include in the message.
            *components (Optional[DiscordComponents]): Components to include in the message.
            poll (Optional[DiscordPoll]): Poll object to include in the message.
            username (Optional[str]): Override the default username of the webhook.
            avatar_url (Optional[str]): Override the default avatar_url of the webhook.
            tts (Optional[bool]): If true, this will be a TTS message.
            wait (Optional[bool]): If true, returns a message else 204 No Content depending.    

        Returns:
            requests.Response: The response from the webhook request.
        """
        if embeds:
            embeds = embeds[:10] 
            embed_dicts = [self._embed_to_dict(embed) for embed in embeds]
        else:
            embed_dicts = []
            
        component_data = components.get_components() if components else []
        poll_data = poll.to_dict() if poll else {}

        payload = {
            "content": content,
            "embeds": embed_dicts,
            "components": component_data,
            "poll": poll_data,
            "tts": tts,
            #"wait": wait
        }
        
        if username:
            payload["username"] = username
        if avatar_url:
            payload["avatar_url"] = avatar_url

        
        response = requests.post(self.webhook_url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response

    def delete_webhook(self) -> requests.Response:
        """
        Delete an existing webhook.

        Returns:
            requests.Response: The response from the webhook request.
        """

        response = requests.delete(self.webhook_url, headers=self.headers)
        response.raise_for_status()
        return response

    def update_webhook(self, webhook_name: Optional[str] = None, avatar_url: Optional[str] = None) -> requests.Response:
        """
        Update an existing webhook.

        Parameters:
            webhook_name (Optional[str]): The new name for the webhook.
            avatar_url (Optional[str]): The new avatar url for the webhook.

        Returns:
            requests.Response: The response from the webhook request.
        """
        payload = {}
        if webhook_name:
            payload["name"] = webhook_name
        if avatar_url:
            payload["avatar"] = avatar_url

        response = requests.patch(self.webhook_url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response

    def get_webhook(self) -> requests.Response:
        """
        Get an existing webhook.

        Returns:
            requests.Response: The response from the webhook request.
        """
        response = requests.get(self.webhook_url, headers=self.headers)
        response.raise_for_status()
        return response