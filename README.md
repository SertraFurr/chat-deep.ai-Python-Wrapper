# chat-deep.ai Python Wrapper

A simple Python wrapper for interacting with chat-deep.ai

## Requirements

```bash
pip install requests
```

## Usage

Run the script:

```bash
python main.py
```

### Commands

- Type your message and press Enter to chat
- `/new` - Start a new chat session
- `/exit` - Quit the application

## Example

```
✅ New session initialized:
  chatId: abc123...
  nonce: xyz789...
  ajaxUrl: https://chat-deep.ai/wp-admin/admin-ajax.php

Type messages below. Type '/new' for a new chat or '/exit' to quit.

You: Hello, how are you?
💬 Server response:
[DeepSeek's response here...]

You: /new
✅ New session initialized:
  chatId: def456...
  ...

You: /exit
👋 Bye.
```

## Note

⚠️ Despite the "DeepSeek" branding and model parameter name, this service actually uses GPT on the backend.

## Disclaimer

This is an unofficial wrapper. The author is not responsible for any misuse or consequences of using this tool. Use at your own risk and in accordance with chat-deep.ai's terms of service.
