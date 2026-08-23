# To-Do List CLI

A command-line to-do list manager built with Python and JSON file storage.

## Features

- **Add** a new task
- **List** all tasks with their completion status
- **Mark** a task as done
- **Delete** a task by id
- **Search** tasks by keyword

## How to Run

No external dependencies — uses only the Python standard library.

```bash
python main.py
```

You'll see a menu where you can choose an action by entering a number (1-6).

## Example Usage

```
1. Add task
2. List tasks
3. Mark task as done
4. Delete task
5. Search tasks
6. Exit
Choose (1-6): 1
Task description: Finish week 4 notes
Task added successfully.

Choose (1-6): 2
--- Task List ---
1. [✘] Finish week 4 notes
```

## Data Storage

Tasks are stored in `tasks.json` in the same folder, as a list of objects:

```json
[
    {
        "id": 1,
        "task": "Finish week 4 notes",
        "done": false,
        "created_at": "2026-08-15"
    }
]
```

The file is created automatically the first time you add a task.

## Concepts Practiced

- Reading and writing JSON files (`json.load`, `json.dump`)
- Error handling for missing or corrupted data files (`try`/`except`, `JSONDecodeError`, `OSError`)
- Rolling back an in-memory change if saving to disk fails, so data stays consistent
- Input validation (empty strings, invalid ids)
- Type hints (`list[dict]`, `Optional[int]`)
- Avoiding repeated code with shared helper functions (DRY principle)
- Using a dictionary to dispatch menu choices instead of a long `if`/`elif` chain

This project builds on the JSON list-handling basics practiced in `exercises-files-api/10-json-list-manager`, extended with proper error handling, rollback logic, and type hints.

## Known Limitations

- Single-user, single-file storage — no support for concurrent access
- No editing of existing task descriptions (only add, complete, delete, search)
- No priority levels or due dates
- No pagination — `list_tasks` prints everything at once