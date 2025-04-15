import json
import os

todo_list = []

DATA_FILE = "todo_list.json"

# Load tasks from file at start
def load_tasks():
    global todo_list
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            todo_list = json.load(f)
    else:
        todo_list = []

# Save tasks to file when exiting
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(todo_list, f, indent=4)

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\n----- YOUR TASKS -----")
        for idx, task in enumerate(todo_list):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx+1}. {task['task']} [{status}]")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added.")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= num < len(todo_list):
            todo_list[num]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(todo_list):
            removed = todo_list.pop(num)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# ==== MAIN ====
load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        save_tasks()
        print("Tasks saved. Exiting To-Do List.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
