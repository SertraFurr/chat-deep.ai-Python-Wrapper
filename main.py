import requests
import re

class DeepSeekChat:
    def __init__(self):
        self.session = requests.Session()
        self.page_url = "https://chat-deep.ai/deepseek-chat/"
        self.nonce = None
        self.chat_id = None
        self.ajax_url = None

    def init_session(self):
        html = self.session.get(self.page_url).text

        self.nonce = re.search(r"const\s+nonce\s*=\s*'([^']+)'", html).group(1)
        self.chat_id = re.search(r"const\s+chatId\s*=\s*'([^']+)'", html).group(1)
        self.ajax_url = re.search(r"const\s+ajaxUrl\s*=\s*'([^']+)'", html).group(1)

        print(f"✅ New session initialized:")
        print(f"  chatId: {self.chat_id}")
        print(f"  nonce: {self.nonce}")
        print(f"  ajaxUrl: {self.ajax_url}")

    def send_message(self, message):
        if not all([self.chat_id, self.nonce, self.ajax_url]):
            print("⚠️ No active session. Use new_session() first.")
            return

        data = {
            "action": "deepseek_chat",
            "message": message,
            "model": "deepseek-reasoner",
            "nonce": self.nonce,
            "save_conversation": "0",
            "session_only": "1",
        }

        response = self.session.post(self.ajax_url, data=data)
        if response.status_code == 200:
            print("💬 Server response:")
            print(response.json()["data"]["response"])
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

    def new_session(self):
        self.init_session()


if __name__ == "__main__":
    chat = DeepSeekChat()
    chat.new_session()

    print("\nType messages below. Type '/new' for a new chat or '/exit' to quit.\n")

    while True:
        msg = input("You: ").strip()
        if msg.lower() == "/exit":
            print("👋 Bye.")
            break
        elif msg.lower() == "/new":
            chat.new_session()
            continue
        elif msg == "":
            continue
        chat.send_message(msg)
