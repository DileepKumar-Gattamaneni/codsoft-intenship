todo_list = {}
def add_task(task):
    if task not in todo_list:
        todo_list[task] = False
        print(f"Task '{task}' added to the to-do list.")
    else:
        print(f"Task '{task}' already exists in the to-do list.")


def complete_task(task):
    if task in todo_list:
        todo_list[task] = True
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


def display_todo_list():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for task, completed in todo_list.items():
            status = "Completed" if completed else "Not Completed"
            print(f"- {task} ({status})")


while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. Display the to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to mark as completed: ")
        complete_task(task)
    elif choice == '3':
        display_todo_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
