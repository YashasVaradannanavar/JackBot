todo_list = []

def show_menu():
    print("\n--- TO-DO LIST BOT ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added ✔️")

    elif choice == "2":
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice. Try again.")
