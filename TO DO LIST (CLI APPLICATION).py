def display_menu():
    print("\n======== YOUR TO DO LIST ==========")
    print("1- ADD A TASK")
    print("2- DELETE A TASK")
    print("3- VIEW ALL TASKS")
    print("4- EXIT THE LIST")


def add_task(tasks):
    task = input("ENTER THE TASK YOU WANT TO ADD: ").strip()
    if task:
        tasks.append(task)
        print(f"YOUR TASK '{task}' ADDED SUCCESSFULLY!")
    else:
        print("Task cannot be empty!")


def delete_task(tasks):
    view_task(tasks)
    if not tasks:
        return

    try:
        task_number = int(
            input("ENTER THE TASK NUMBER YOU WANT TO DELETE: ")
        )
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"TASK '{removed_task}' REMOVED SUCCESSFULLY!")
        else:
            print("INVALID TASK NUMBER, TRY A VALID NUMBER!")
    except ValueError:
        print("INVALID INPUT! Please enter a valid number.")


def view_task(tasks):
    if not tasks:
        print("NO TASKS ADDED YET!")
    else:
        print("\n===== YOUR TO DO LIST =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index} : {task}")


def todo_list_app():
    tasks = []
    while True:
        display_menu()
        choice = input("ENTER YOUR CHOICE (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            view_task(tasks)
        elif choice == "4":
            print("EXITING THE LIST! SEE YOU AGAIN ^ - ^")
            break
        else:
            print("INVALID CHOICE !!! ENTER SOMETHING BETWEEN 1-4")


if __name__ == "__main__":
    todo_list_app()
