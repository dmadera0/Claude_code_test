# Todo App

A simple command-line todo application written in Python. Manage your tasks with add, list, and delete commands. All todos are automatically saved to a JSON file for persistence.

## Features

- **Add todos**: Quickly add new tasks from the command line
- **List todos**: View all your todos with their IDs and status
- **Delete todos**: Remove completed or unwanted tasks by ID
- **Persistent storage**: Todos are saved to a JSON file and persist between sessions
- **Timestamps**: Each todo records when it was created
- **Simple interface**: Easy-to-use command-line interface

## Installation

1. Ensure you have Python 3.6+ installed
2. Download or clone this repository
3. No external dependencies required - uses only Python's standard library

## Usage

### Add a Todo

```bash
python3 todo.py add "Your task description"
```

Example:
```bash
python3 todo.py add "Buy groceries"
python3 todo.py add "Finish project report"
```

### List All Todos

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

### Delete a Todo

```bash
python3 todo.py delete <id>
```

Example:
```bash
python3 todo.py delete 2
```

This removes the todo with ID 2.

## Data Storage

Todos are stored in a JSON file located at:
```
~/.todos.json
```

Each todo contains:
- **id**: Unique identifier for the todo
- **task**: The description of the task
- **completed**: Boolean flag (currently set to false)
- **created**: ISO timestamp of when the todo was created

Example JSON structure:
```json
[
  {
    "id": 1,
    "task": "Buy groceries",
    "completed": false,
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

## How It Works

1. **Load**: When you run a command, the app loads existing todos from `~/.todos.json`
2. **Process**: The app executes your command (add, list, or delete)
3. **Save**: For add and delete operations, the updated todo list is saved back to the JSON file
4. **Display**: The app provides feedback about what was done

## Command Reference

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add` | `<task>` | Add a new todo with the given task description |
| `list` | None | Display all todos with their IDs and completion status |
| `delete` | `<id>` | Delete the todo with the specified ID |

## Requirements

- Python 3.6 or higher
- Standard library modules: `json`, `sys`, `pathlib`, `datetime`, `argparse`

## License

Free to use and modify as needed.
