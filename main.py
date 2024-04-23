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







