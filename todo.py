tasks = []

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added")
    else:
        print("Task cannot be empty")

elif choice == "3":
    num = int(input("Enter task number: "))
    tasks[num-1]["done"] = True
    print("Task marked complete")

