#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from datetime import datetime
import argparse


TODO_FILE = Path.home() / ".todos.json"


def load_todos():
    """Load todos from JSON file."""
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    """Save todos to JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add_todo(task):
    """Add a new todo."""
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "task": task,
        "completed": False,
        "created": datetime.now().isoformat()
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✓ Added: {task}")


def list_todos():
    """List all todos."""
    todos = load_todos()
    if not todos:
        print("No todos yet!")
        return

    print("\nYour todos:")
    print("-" * 60)
    for todo in todos:
        status = "✓" if todo["completed"] else "○"
        print(f"{status} [{todo['id']}] {todo['task']}")
    print("-" * 60)
    print(f"Total: {len(todos)} todo(s)\n")


def delete_todo(todo_id):
    """Delete a todo by ID."""
    todos = load_todos()
    original_count = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]

    if len(todos) == original_count:
        print(f"Todo with ID {todo_id} not found.")
        return

    save_todos(todos)
    print(f"✓ Deleted todo #{todo_id}")


def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line todo app",
        prog="todo"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("task", help="The task to add")

    # List command
    subparsers.add_parser("list", help="List all todos")

    # Delete command
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
    elif args.command == "delete":
        delete_todo(args.id)


if __name__ == "__main__":
    main()
