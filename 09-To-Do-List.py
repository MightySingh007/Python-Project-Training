todo_list = []
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_no - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
