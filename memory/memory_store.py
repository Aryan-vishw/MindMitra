import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("data/user_mood_memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as file:
            try:
                content = file.read().strip()
                if not content:
                    return {}
                return json.loads(content)
            except json.JSONDecodeError:
                # Log or warn if needed
                return {}
    return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_last_mood(user_id="default_user"):
    memory = load_memory()
    user_data = memory.get(user_id, {})
    return user_data.get("last_mood")

def set_last_mood(mood, user_id="default_user"):
    memory = load_memory()
    memory[user_id] = {
        "last_mood": mood,
        "last_updated": datetime.now().isoformat()
    }
    save_memory(memory)

def get_full_history(user_id="default_user"):
    memory = load_memory()
    return memory.get(user_id, {})
