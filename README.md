# Todo CLI

A lightweight command-line todo application written in Python. Add, list, complete, and delete tasks — all persisted locally in a JSON file.

## Features

- **Add todos**: Quickly add new tasks from the command line
- **List todos**: View all tasks with their IDs and completion status
- **Complete todos**: Mark tasks as done without removing them
- **Delete todos**: Remove tasks by ID
- **Persistent storage**: Todos are saved to `~/.todos.json` and survive between sessions
- **Unique IDs**: IDs are never reused, even after deletion
- **No dependencies**: Uses only Python's standard library

## Requirements

- Python 3.6 or higher

## Installation

### Run directly

```bash
python3 todo.py <command>
```

### Install as a CLI tool

```bash
pip install .
todo <command>
```

## Usage

### Add a todo

```bash
python3 todo.py add "Buy groceries"
```

### List all todos

```bash
python3 todo.py list
```

Output:
```
Your todos:
------------------------------------------------------------
○ [1] Buy groceries
○ [2] Finish project report
------------------------------------------------------------
Total: 2 todo(s)
```

### Complete a todo

```bash
python3 todo.py complete 1
```

The todo remains visible in `list` output and is marked with `✓`.

### Delete a todo

```bash
python3 todo.py delete 2
```

## Command Reference

| Command    | Arguments | Description                          |
|------------|-----------|--------------------------------------|
| `add`      | `<task>`  | Add a new todo                       |
| `list`     | —         | Display all todos                    |
| `complete` | `<id>`    | Mark the todo with the given ID done |
| `delete`   | `<id>`    | Remove the todo with the given ID    |

## Data Storage

Todos are stored in `~/.todos.json`. Example:

```json
[
  {
    "id": 1,
    "task": "Buy groceries",
    "completed": true,
    "created": "2026-02-25T14:13:03.972292"
  },
  {
    "id": 3,
    "task": "Call dentist",
    "completed": false,
    "created": "2026-02-25T14:13:52.273644"
  }
]
```

## License

MIT
