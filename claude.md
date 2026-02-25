# Project: Todo CLI

A single-file Python CLI tool for managing tasks locally.

## Architecture

- **`todo.py`** — entire application; no external dependencies
- **`~/.todos.json`** — persistent storage (user's home directory, not in repo)
- **`pyproject.toml`** — packaging config; `pip install .` exposes a `todo` entry point

## Key Design Decisions

- IDs are generated with `max(existing_ids) + 1` — never reused after deletion
- Errors (bad JSON, missing ID, file write failure) exit with a non-zero status code and print to stderr
- The `completed` field is set by `complete`, not deleted — full history is preserved

## Commands

| Command    | Function        |
|------------|-----------------|
| `add`      | `add_todo()`    |
| `list`     | `list_todos()`  |
| `complete` | `complete_todo()` |
| `delete`   | `delete_todo()` |

## Common Tasks

Run the app:
```bash
python3 todo.py list
```

Install locally:
```bash
pip install .
todo list
```
