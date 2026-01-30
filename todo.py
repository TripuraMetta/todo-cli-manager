tasks = []

def menu():
    print("\n====== TO-DO LIST MANAGER ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ").strip()

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append({"task": task, "done": False})
            print("Task added successfully!")
        else:
            print("Task cannot be empty")

    # VIEW TASKS
    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✔ Completed" if t["done"] else "✖ Pending"
                print(f"{i}. {t['task']} [{status}]")

    # MARK TASK AS COMPLETE

elif choice == "3":
    try:
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as completed")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")


    # DELETE TASK
    elif choice == "4":
        if not tasks:
            print("No tasks to delete")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)
                    print(f"Deleted task: {deleted['task']}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")

    # EXIT
    elif choice == "5":
        print("Exiting To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
