#----------
# Домашнее задание №2
#----------
# Задание: Работа csv

# 1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
#    В списке нужно создать не менее 4-х словарей
# 2. Запишите содержимое списка словарей в файл в формате csv

import csv

def main():
    users_data = [
        {'name': 'Maria', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Vasya', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Eduard', 'age': 48, 'job': 'Big boss'},
        {'name': 'Irina', 'age': 25, 'job': 'Teacher'}
        ]

    with open ('users_data.csv', 'w', encoding='utf-8') as data:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(data, fields, delimiter=';')
        writer.writeheader()

        for user in users_data:
            writer.writerow(user)

if __name__ == "__main__":
    main()
