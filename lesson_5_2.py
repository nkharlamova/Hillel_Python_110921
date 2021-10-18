import random


# функции

def create_random_int_number_list(len_list=5):
    numbers = [random.randint(1, 10) for _ in range(len_list)]
    return numbers


def print_dict(some_dict):  # ВСЕ ЧТО ИСПОЛЬЗУЕМ - ПЕРЕДАЕМ В ФУНКЦИЮ!!!
    for key, value in some_dict.items():
        print(f"{key}: {value}")


my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
person = {"name": "John", "age": 23, "sex": "Male", }

# print(person)
# print_dict(person)
# print_dict(some_dict=my_dict)
len_list = random.randint(10, 20)
result = create_random_int_number_list()
print(result)

# использование модулей, пакетов, библиотек
import random  # импорт всего модуля
# from random import randint  # импорт конкретной функции
from string import ascii_lowercase as alphabet

# value = random.randint(1, 10)
# print(value)
# my_list = ["True", "False", "Unknown"]
# my_choice = random.choice(my_list)
# print(my_choice)

# alphabet_list = list(alphabet)
# print(alphabet_list, type(alphabet_list))
#
# random.shuffle(alphabet_list)
# print(alphabet_list)


# my_temp_dict = {11: 1, 12: 2, 13: 3}
# print(my_temp_dict)
#
# if len(my_temp_dict.values()) == len(set(my_temp_dict.values())) :
#     temp_revers_dict = {value: key for key, value in my_temp_dict.items()}
#     print(temp_revers_dict)

# my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
# res = []
# for symb in set(my_str):
#     if my_str.count(symb) == 1:
#        res.append(symb)
# print(res)