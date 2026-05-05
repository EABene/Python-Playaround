import os
import json

# Datei erstellen falls nicht vorhanden
if not os.path.exists("habits.json"):
    with open ("habits.json", "w") as f:
        json.dump({}, f)