import os
from pathlib import Path
import json

FILE_PATH = Path(__file__).parent / "habits.json"

if not FILE_PATH.exists():
    with open(FILE_PATH, "w") as f:
        json.dump({}, f)


data = {"Paul": 2, "John": 3}

with open(FILE_PATH, "w") as f:
    json.dump(data, f, indent=2)

print("done")