from pathlib import Path
def total_salary(path):
    total_salary = 0
    total_developers = 0
    try:
        with open(path, 'r') as file:
            for line in file:
                _, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary
                total_developers += 1
        average_salary = total_salary / total_developers
        return total_salary, average_salary
    except FileNotFoundError:
        print("File not found")


total, average = total_salary('data.txt')
print("Total salary:", total)
print("Average salary:", average)

# Завдання 2

from pathlib import Path
def get_cats_info(path):
    cats_info = []  # Створюємо пустий список для зберігання інформації про котів
    try:
        with open(path, 'r') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')  # Розбиваємо рядок на частини за комами
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cats_info.append(cat_info)  # Додаємо словник до списку
    except FileNotFoundError:
        print("File not found")
    return cats_info

# Приклад використання:
cats = get_cats_info('cats.txt')
for cat in cats:
    print(cat)

# 3
from pathlib import Path
def parse_input(user_input):
    tokens = user_input.split()
    command = tokens[0].lower()  # перший елемент - команда
    args = tokens[1:]  # решта елементів - аргументи
    return command, args
contacts = {}
def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added.")
def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")
def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")


def show_all():
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")


def main():
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            add_contact(*args)
        elif command == "change":
            change_contact(*args)
        elif command == "phone":
            show_phone(*args)
        elif command == "all":
            show_all()
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
