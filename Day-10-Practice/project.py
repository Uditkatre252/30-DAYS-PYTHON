# To-Do list

lst = list()

def add_task(n):
    lst.append(n)
    print(f"Task added: {lst}")

def delete_task(n):
    if n in lst:
        lst.remove(n)
        print(f"Task removed: {lst}")
    else:
        print(f"Task not found: {n}")
def show_tasks():
    if not lst:
        print("No tasks added")
    else:
        print(f"Tasks added: {lst}")



while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input('Enter your task: ')
        add_task(task)

    elif choice == 2:
        task = input('Enter your task: ')
        delete_task(task)

    elif choice == 3:
        print(lst)

    elif choice == 4:
        break

    else:
        print("Invalid choice")











