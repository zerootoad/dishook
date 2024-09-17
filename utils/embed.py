from typing import Optional, Dict, List, Any, Union
from datetime import datetime

class DiscordEmbed:
    """
    A class for creating Discord Embeds.
    """

    def __init__(self, 
                 title: Optional[str] = None, 
                 description: Optional[str] = None, 
                 **kwargs: Any) -> None:
        """
        Initialize a Discord Embed method.

        Parameters:
            title (Optional[str]): The title of the embed.
            description (Optional[str]): The description of the embed.
            **kwargs (Any): Additional parameters for the embed, such as:
                - author (Dict[str, Any]): Details about the author.
                - color (Union[str, int]): Color of the embed in decimal or hex.
                - fields (List[Dict[str, Any]]): A list of field dictionaries.
                - footer (Dict[str, Any]): Information for the footer.
                - image (Dict[str, Any]): Details about the image.
                - provider (Dict[str, Any]): Provider information.
                - thumbnail (Dict[str, Any]): Thumbnail details.
                - timestamp (Union[float, int, str, datetime]): Timestamp for the embed.
                - url (str): URL making the title a clickable link.
                - video (Dict[str, Any]): Video details.
        """
        self.title = title
        self.description = description
        self.url = kwargs.get("url")
        self.footer = kwargs.get("footer")
        self.image = kwargs.get("image")
        self.thumbnail = kwargs.get("thumbnail")
        self.video = kwargs.get("video")
        self.provider = kwargs.get("provider")
        self.author = kwargs.get("author")
        self.fields = kwargs.get("fields", [])
        self.color = None
        self.timestamp = None

        self.set_color(kwargs.get("color"))
        self.set_timestamp(kwargs.get("timestamp"))

    def set_title(self, title: str) -> None:
        """
        Set the title of the embed.

        Parameters:
            title (str): The title to set.
        """
        self.title = title

    def set_description(self, description: str) -> None:
        """
        Set the description of the embed.

        Parameters:
            description (str): The description to set.
        """
        self.description = description

    def set_url(self, url: str) -> None:
        """
        Set the URL for the embed title to make it clickable.

        Parameters:
            url (str): The URL to set.
        """
        self.url = url

    def set_timestamp(self, timestamp: Optional[Union[float, int, str, datetime]] = None) -> None:
        """
        Set the timestamp for the embed.

        Parameters:
            timestamp (Optional[Union[float, int, str, datetime]]): The timestamp to set. If None, uses the current time.
        """
        if timestamp is None:
            timestamp = datetime.utcnow()
        elif isinstance(timestamp, (float, int)):
            timestamp = datetime.utcfromtimestamp(timestamp)
        elif isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        self.timestamp = timestamp.isoformat()

    def set_color(self, color: Optional[Union[str, int]] = None) -> None:
        """
        Set the color of the embed.

        Parameters:
            color (Optional[Union[str, int]]): The color of the embed in hexadecimal or decimal format.
        """
        if color is not None:
            if isinstance(color, str):
                color = int(color, 16)
            if not (0 <= color < 16777216):
                raise ValueError(f"Color {color} is out of the valid range.")
            self.color = color

    def set_footer(self, text: str, icon_url: Optional[str] = None) -> None:
        """
        Set the footer of the embed.

        Parameters:
            text (str): The text of the footer.
            icon_url (Optional[str]): URL of the footer icon.
        """
        self.footer = {"text": text, "icon_url": icon_url}

    def set_image(self, url: str, height: Optional[int] = None, width: Optional[int] = None) -> None:
        """
        Set the image of the embed.

        Parameters:
            url (str): URL of the image.
            height (Optional[int]): Height of the image.
            width (Optional[int]): Width of the image.
        """
        self.image = {"url": url, "height": height, "width": width}

    def set_thumbnail(self, url: str, height: Optional[int] = None, width: Optional[int] = None) -> None:
        """
        Set the thumbnail of the embed.

        Parameters:
            url (str): URL of the thumbnail.
            height (Optional[int]): Height of the thumbnail.
            width (Optional[int]): Width of the thumbnail.
        """
        self.thumbnail = {"url": url, "height": height, "width": width}

    def set_video(self, url: str, height: Optional[int] = None, width: Optional[int] = None) -> None:
        """
        Set the video of the embed.

        Parameters:
            url (str): URL of the video.
            height (Optional[int]): Height of the video.
            width (Optional[int]): Width of the video.
        """
        self.video = {"url": url, "height": height, "width": width}

    def set_provider(self, name: Optional[str] = None, url: Optional[str] = None) -> None:
        """
        Set the provider information of the embed.

        Parameters:
            name (Optional[str]): Name of the provider.
            url (Optional[str]): URL of the provider.
        """
        self.provider = {"name": name, "url": url}

    def set_author(self, name: str, url: Optional[str] = None, icon_url: Optional[str] = None) -> None:
        """
        Set the author information of the embed.

        Parameters:
            name (str): Name of the author.
            url (Optional[str]): URL of the author.
            icon_url (Optional[str]): Icon URL of the author.
        """
        self.author = {"name": name, "url": url, "icon_url": icon_url}

    def add_field(self, name: str, value: str, inline: bool = True) -> None:
        """
        Add a field to the embed.

        Parameters:
            name (str): Name of the field.
            value (str): Value of the field.
            inline (bool): Whether the field is inline with other fields. Default is True.
        """
        self.fields.append({"name": name, "value": value, "inline": inline})

    def remove_field(self, index: int) -> None:
        """
        Remove a field from the embed by index.

        Parameters:
            index (int): Index of the field to remove.
        """
        if 0 <= index < len(self.fields):
            self.fields.pop(index)
        else:
            raise IndexError("Field index out of range.")

    def get_fields(self) -> List[Dict[str, Any]]:
        """
        Get all fields of the embed.

        Returns:
            List[Dict[str, Any]]: List of fields in the embed.
        """
        return self.fields

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the embed object to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the embed.
        """
        embed = {
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "footer": self.footer,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "video": self.video,
            "provider": self.provider,
            "author": self.author,
            "fields": self.fields,
        }
        return {k: v for k, v in embed.items() if v is not None}
