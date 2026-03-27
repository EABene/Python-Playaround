# to do list app

import json
import sys
import os

FILE = "todos.json"

# utility functions

def load_todos():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)

# usability functions

def add_task(title):
    todos = load_todos()
    task = {"id": len(todos) + 1, "title": title, "done": False}
    todos.append(task)
    save_todos(todos)
    print(f"✅ Hinzugefügt: {title}")


def list_tasks():
    todos = load_todos()
    if not todos:
        print("Keine Aufgaben vorhanden.")
        return
    for task in todos:
        status = "✓" if task["done"] else "✗"
        print(f"[{status}] {task['id']}. {task['title']}")


def complete_task(task_id):
    todos = load_todos()
    for task in todos:
        if task["id"] == task_id:
            task["done"] = True
            save_todos(todos)
            print(f"🎉 Erledigt: {task['title']}")
            return
    print(f"Aufgabe {task_id} nicht gefunden.")


def delete_task(task_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != task_id]
    save_todos(todos)
    print(f"🗑️  Aufgabe {task_id} gelöscht.")


def print_help():
    print("""
Verwendung:
  python todo.py add "Aufgabe"   → Aufgabe hinzufügen
  python todo.py list            → Alle Aufgaben anzeigen
  python todo.py done <id>       → Aufgabe als erledigt markieren
  python todo.py delete <id>     → Aufgabe löschen
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(sys.argv[2])
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) >= 3:
        complete_task(int(sys.argv[2]))
    elif command == "delete" and len(sys.argv) >= 3:
        delete_task(int(sys.argv[2]))
    else:
        print_help()