# форматы json, csv
# импорт из файлов
# assert
# функции сортировки
# регулярные выражения (введение)

import re

my_str = "c.965 – c. 1040 "

numbers = re.findall(r"[0-9]+", my_str)
print(numbers)


###################### функции сортировки

def sort_by_age(person_dict):
    age = person_dict["age"]
    return age


def sort_by_len_name(person_dict):
    name = person_dict["name"]
    return len(name)


def sort_by_len_name_and_age(person_dict):
    name = person_dict["name"]
    age = person_dict["age"]
    return len(name), age


persons = [{"name": "John", "age": 55},
           {"name": "Anna", "age": 23},
           {"name": "Dan", "age": 5},
           {"name": "Maximusss", "age": 24},
           {"name": "Olgha", "age": 25},
           {"name": "Volodymyr", "age": 5},
           {"name": "Jack", "age": 45}]

sort_person_by_age = sorted(persons, key=sort_by_age)
print(sort_person_by_age)

sort_person_by_len_name = sorted(persons, key=sort_by_len_name)
print(sort_person_by_len_name)

sort_person_by_len_name_and_age = sorted(persons, key=sort_by_len_name_and_age)
print(sort_person_by_len_name_and_age)

temperature = [-2, -4, -6, -3, 0, 3, 5, -1, -4]
sort_temp = sorted(temperature, key=abs)
print(sort_temp)

words = ['ajsyg', 'jasy', 'Qe', '124', 'jhz<zjgzsdjsdyg', 'd']

sort_words = sorted(words, key=len)
print(sort_words)

########################################

price = -10
assert price > 0, "Negative price"
value_coef = 100 / price
print(value_coef)


################################## импорт из файлов
from lesson7_func import create_email

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print("!!!!", e_mail)

print(f"{__name__=}")

############################
import json

def read_json(filename):
    with open(filename, "r") as file:
        some_data = json.load(file)
        return some_data


def write_json(filename, some_data, indent=None):
    with open(filename, "w") as file:
        json.dump(some_data, file, indent=indent)


filename = "some_data.json"
data = read_json(filename)
print(data)

# data["name"] = "John"
# write_json(filename, data, 8)

my_list = [1, 2, 3]

my_list_str_json = json.dumps(my_list)
print(my_list_str_json, type(my_list_str_json))

new_list = json.loads(my_list_str_json)
print(new_list[0])

################################### csv
import csv

filename = "test_2.csv"

with open(filename, 'r', encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')  # считывает всегда в виде строк
    data = []
    for row in reader:
        data.append(row)

print(data)
data.append([10, 11, 12])

with open("test_2.csv", 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

with open(filename, 'r', encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    data = []
    for row in reader:
        data.append(row)

for row in data:
    row["Total"] = int(row["Total"]) + 10
print(data)

with open("test_3.csv", 'w', encoding="utf-8") as csv_file:
    # fieldnames = list(data[0].keys())
    fieldnames = ['Column_1', 'Column_2', 'Column_3', 'Total']
    print(f"{fieldnames=}")
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)