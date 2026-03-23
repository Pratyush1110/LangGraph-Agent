import json
import os
from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage

HISTORY_FILE = "chat_history.json"


def save_history(messages: list):
    """Serialize LangChain messages to JSON and write to disk."""
    serialized = []
    for msg in messages:
        serialized.append(
            {
                "role": "human" if isinstance(msg, HumanMessage) else "ai",
                "content": msg.content,
                "timestamp": datetime.now().isoformat(),
            }
        )

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(serialized, f, indent=2)

    print(f"[Memory] Saved {len(serialized)} messages to {HISTORY_FILE}")


def load_history() -> list:
    """Load messages from disk and reconstruct LangChain message objects."""
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, encoding="utf-8") as f:
        data = json.load(f)

    messages = []
    for item in data:
        if item.get("role") == "human":
            messages.append(HumanMessage(content=item.get("content", "")))
        else:
            messages.append(AIMessage(content=item.get("content", "")))

    print(f"[Memory] Loaded {len(messages)} messages from previous session")
    return messages


def clear_history():
    """Wipe saved history."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("[Memory] History cleared.")
