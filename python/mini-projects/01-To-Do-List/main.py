import json
import os
from datetime import date
from typing import Optional

TASKS_FILE = "tasks.json"


def load_tasks() -> list[dict]:
    """
    Loads tasks from the JSON file.
    If the file doesn't exist -> return an empty list.
    If the file is corrupted/incomplete -> warn instead of crashing,
    and return an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted or invalid. Starting with an empty list.\n")
        return []
    except OSError as e:
        print(f"Error reading file: {e}\n")
        return []

    if not isinstance(data, list):
        print("Warning: tasks.json has an invalid structure. Starting with an empty list.\n")
        return []

    return data


def save_tasks(tasks: list[dict]) -> bool:
    """Saves tasks to disk. Returns bool so the caller knows if it succeeded."""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"Error saving file: {e}\n")
        return False


def get_next_id(tasks: list[dict]) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def get_valid_text(prompt: str) -> str:
    """Gets text input and ensures it's not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def get_valid_id(prompt: str) -> Optional[int]:
    """Gets an id input; returns None instead of crashing if it's invalid."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Please enter a valid number.\n")
        return None


def add_task(tasks: list[dict]) -> None:
    description = get_valid_text("Task description: ")

    new_task = {
        "id": get_next_id(tasks),
        "task": description,
        "done": False,
        "created_at": str(date.today()),
    }

    tasks.append(new_task)
    if save_tasks(tasks):
        print("Task added successfully.\n")
    else:
        tasks.remove(new_task)   # rollback if saving failed


def list_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks found.\n")
        return

    print("--- Task List ---")
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        print(f"{task['id']}. [{status}] {task['task']}")
    print()


def find_task_by_id(tasks: list[dict], task_id: int) -> Optional[dict]:
    return next((task for task in tasks if task["id"] == task_id), None)


def complete_task(tasks: list[dict]) -> None:
    """Marks a task as done by id."""
    list_tasks(tasks)
    if not tasks:
        return

    task_id = get_valid_id("Task id to mark as done: ")
    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("No task found with that id.\n")
        return

    previous_state = task["done"]   # remember in case we need to roll back
    task["done"] = True

    if save_tasks(tasks):
        print("Task marked as done.\n")
    else:
        task["done"] = previous_state   # rollback if saving failed


def delete_task(tasks: list[dict]) -> None:
    list_tasks(tasks)
    if not tasks:
        return

    task_id = get_valid_id("Task id to delete: ")
    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("No task found with that id.\n")
        return

    tasks.remove(task)
    if not save_tasks(tasks):
        tasks.append(task)   # rollback if saving failed
        return

    print("Task deleted.\n")


def search_tasks(tasks: list[dict]) -> None:
    keyword = get_valid_text("Search keyword: ").lower()

    results = [task for task in tasks if keyword in task["task"].lower()]

    if not results:
        print("No results found.\n")
        return

    print(f"--- {len(results)} result(s) found ---")
    for task in results:
        status = "✔" if task["done"] else "✘"
        print(f"{task['id']}. [{status}] {task['task']}")
    print()


def show_menu() -> None:
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Search tasks")
    print("6. Exit")


def main() -> None:
    tasks = load_tasks()

    actions = {
        "1": add_task,
        "2": list_tasks,
        "3": complete_task,
        "4": delete_task,
        "5": search_tasks,
    }

    while True:
        show_menu()
        choice = input("Choose (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice](tasks)
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()