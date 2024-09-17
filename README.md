# Dishook (W.I.P)

**Dishook** is a simple and easy-to-use Python library for working with Discord webhooks. It provides convenient utilities for sending webhooks, creating rich embeds, handling allowed mentions, and more. This library is perfect for developers who want to automate sending messages, embeds, and polls to Discord channels with minimal setup.

## Features

- **Webhook Sending**: Easily send webhooks to Discord channels.
- **Embed Creation**: Build rich, customizable Discord embeds.
- **Polls**: Create and manage interactive Discord polls via webhooks.
- **Allowed Mentions**: Safely control how users, roles, and everyone mentions are handled.
- **Component Support**: Add buttons and interactive components to your webhook messages.

## Installation

To install **Dishook**, simply clone this repository and include the `utils` module in your project.

```bash
git clone https://github.com/yourusername/dishook
cd dishook
```

## Usage

Here’s a quick example of how to send a simple webhook using **Dishook**:

```python
from utils.webhook import Webhook
from utils.embed import Embed

# Create a webhook instance
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
webhook = Webhook(url=webhook_url)

# Create a basic embed
embed = Embed(title="Hello, Discord!", description="This is a test message.")

# Send the embed via webhook
webhook.send(embed=embed)
```

## Available Modules

- `webhook.py`: Handles sending messages, embeds, and components via webhooks.
- `embed.py`: Utility for creating rich embeds in Discord messages.
- `poll.py`: Create interactive polls and send them via webhooks.
- `allowed_mentions.py`: Control how mentions work (users, roles, everyone).
- `components.py`: Add buttons, dropdowns, and other interactive components to webhooks.
- `utilities.py`: Miscellaneous helper functions used across the library.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
