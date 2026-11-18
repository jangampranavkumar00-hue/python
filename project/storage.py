
import json
import os
from datetime import datetime

FILE = "passwords.json"

def load_records():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_record(strength):
    records = load_records()

    records.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "strength": strength
    })

    with open(FILE, "w") as f:
        json.dump(records, f, indent=4)

def search_records(keyword):
    records = load_records()
    return [
        record for record in records
        if keyword.lower() in record["strength"].lower()
    ]
