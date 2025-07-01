import json
from pathlib import Path
from config.config import OUTPUT_PATH

def save_to_json(data: list[dict], filename: str = OUTPUT_PATH) -> None:
    Path("data").mkdir(exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json(filename: str = OUTPUT_PATH) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)