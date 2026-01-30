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

elif choice == "2":
    if not tasks:
        print("No tasks found")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✔" if t["done"] else "✖"
            print(f"{i}. {t['task']} [{status}]")

