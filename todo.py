tasks = []

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

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

elif choice == "4":
    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1)
    print("Task deleted")

