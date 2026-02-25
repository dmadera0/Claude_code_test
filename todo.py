#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from datetime import datetime
import argparse


TODO_FILE = Path.home() / ".todos.json"


def load_todos():
    """Load todos from JSON file."""
    if not TODO_FILE.exists():
        return []
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error reading todos file: {e}", file=sys.stderr)
        sys.exit(1)


def save_todos(todos):
    """Save todos to JSON file."""
    try:
        with open(TODO_FILE, "w") as f:
            json.dump(todos, f, indent=2)
    except OSError as e:
        print(f"Error saving todos: {e}", file=sys.stderr)
        sys.exit(1)


def next_id(todos):
    """Return the next available unique ID."""
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1


def add_todo(task):
    """Add a new todo."""
    todos = load_todos()
    todo = {
        "id": next_id(todos),
        "task": task,
        "completed": False,
        "created": datetime.now().isoformat(),
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✓ Added: {task}")


def list_todos():
    """List all todos."""
    todos = load_todos()
    if not todos:
        print("No todos yet.")
        return

    print("\nYour todos:")
    print("-" * 60)
    for todo in todos:
        status = "✓" if todo["completed"] else "○"
        print(f"{status} [{todo['id']}] {todo['task']}")
    print("-" * 60)
    print(f"Total: {len(todos)} todo(s)\n")


def complete_todo(todo_id):
    """Mark a todo as completed."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["completed"]:
                print(f"Todo #{todo_id} is already completed.")
                return
            todo["completed"] = True
            save_todos(todos)
            print(f"✓ Completed todo #{todo_id}: {todo['task']}")
            return
    print(f"Todo with ID {todo_id} not found.", file=sys.stderr)
    sys.exit(1)


def delete_todo(todo_id):
    """Delete a todo by ID."""
    todos = load_todos()
    original_count = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]

    if len(todos) == original_count:
        print(f"Todo with ID {todo_id} not found.", file=sys.stderr)
        sys.exit(1)

    save_todos(todos)
    print(f"✓ Deleted todo #{todo_id}")


def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line todo app",
        prog="todo",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("task", help="The task to add")

    subparsers.add_parser("list", help="List all todos")

    complete_parser = subparsers.add_parser("complete", help="Mark a todo as completed")
    complete_parser.add_argument("id", type=int, help="ID of the todo to complete")

    delete_parser = subparsers.add_parser("delete", help="Delete a todo by ID")
    delete_parser.add_argument("id", type=int, help="ID of the todo to delete")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "add":
        add_todo(args.task)
    elif args.command == "list":
        list_todos()
    elif args.command == "complete":
        complete_todo(args.id)
    elif args.command == "delete":
        delete_todo(args.id)


if __name__ == "__main__":
    main()
