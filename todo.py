tasks = []

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
