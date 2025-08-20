'''
Build a to-do list app where tasks are saved to a file and loaded when the
program restarts.
'''

import os

filename1 = r'C:\Users\chuda\OneDrive\Desktop\TICKET TO USA\QUANTUMBOT\PYTHON\Intermediate\todo.txt'
filename2 = r'C:\Users\chuda\OneDrive\Desktop\TICKET TO USA\QUANTUMBOT\PYTHON\Intermediate\updated_todo.txt'

def load_tasks():
    tasks = []
    if os.path.exists(filename1):
        with open(filename1, "r") as f:
            for line in f:
                task, status = line.strip().rsplit(":", 1)
                tasks.append({'task': task, 'done': status == 'done'})
    return tasks

def save_tasks(tasks):
    with open(filename2, "w") as f:
        for t in tasks:
            line = f"{t['task']}:{'done' if t['done'] else 'not_done'}\n"
            f.write(line)

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    tasks.append({'task': task, 'done': False})
    print("Task added.")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTo-Do List:")
        for i, t in enumerate(tasks, 1):
            status = "done" if t['done'] else "not done"
            print(f"{i}. {t['task']} {status}")

def mark_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():

    tasks = load_tasks()

    while True:

        print("\nToDo List")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()