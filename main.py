import os
import json
from datetime import datetime

# Path(s)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_NAME = "loggFiles"
FOLDER_PATH = os.path.join(BASE_DIR, FOLDER_NAME)
INDEX_PATH = os.path.join(FOLDER_PATH, "index.json")

os.makedirs(FOLDER_PATH, exist_ok=True)


def load_index():
    if not os.path.exists(INDEX_PATH):
        return []
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_index(entries):
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


# create entry

def create_entry():
    print("\n--- New entry ---")
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    print("Write your entry. End with a single line containing only '1"
          ":end")
    lines = []
    while True:
        line = input()
        if line.strip() == ":end":
            break
        lines.append(line)

    content = "\n".join(lines)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.txt"
    file_path = os.path.join(FOLDER_PATH, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    entries = load_index()
    entries.append({
        "title": title,
        "timestamp": timestamp,
        "filename": filename
    })
    save_index(entries)

    print(f"\nEntry saved as: {filename}")


def list_entries():
    entries = load_index()
    if not entries:
        print("\nNo entries yet.")
        return

    print("\n--- Entries ---")
    for i, e in enumerate(entries, start=1):
        print(f"[{i}] {e['title']} ({e['timestamp']})")


def view_entry():
    entries = load_index()
    if not entries:
        print("\nNo entries to view.")
        return

    list_entries()
    try:
        choice = int(input("\nWhich entry number to view? ")) - 1
    except ValueError:
        print("Invalid input.")
        return

    if not (0 <= choice < len(entries)):
        print("Invalid choice.")
        return

    entry = entries[choice]
    file_path = os.path.join(FOLDER_PATH, entry["filename"])

    if not os.path.exists(file_path):
        print("File missing on disk.")
        return

    print(f"\n--- {entry['title']} ({entry['timestamp']}) ---\n")
    with open(file_path, "r", encoding="utf-8") as f:
        print(f.read())


def delete_entry():
    entries = load_index()
    if not entries:
        print("\nNo entries to delete.")
        return

    list_entries()
    try:
        choice = int(input("\nWhich entry number to delete? ")) - 1
    except ValueError:
        print("Invalid input.")
        return

    if not (0 <= choice < len(entries)):
        print("Invalid choice.")
        return

    entry = entries.pop(choice)
    save_index(entries)

    file_path = os.path.join(FOLDER_PATH, entry["filename"])
    if os.path.exists(file_path):
        os.remove(file_path)

    print(f"Deleted entry: {entry['title']}")


# ---------- Menu loop ----------

def main():
    while True:
        print("\n======================")
        print("      JOURNAL APP     ")
        print("======================")
        print("[1] New entry")
        print("[2] List entries")
        print("[3] View entry")
        print("[4] Delete entry")
        print("[5] Exit")

        choice = input("> ").strip()

        if choice == "1":
            create_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            view_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()
