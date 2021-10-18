# Словари, методы словарей
# модули
# функции

######################### словари
my_dict = {"name": "John", "age": 23}  # изменяемый, итерируемый тип данных. Порядок ключей не гарантируется!
print(my_dict, type(my_dict))
print(my_dict["name"])
print(my_dict.get(111))

########################### конструирование сложных словарей
address = {"city": "Dnipro", "street": "Polya", "ZIP": 49000}
skils = {"hard": ["python", "html", "DB", "C++"], "soft": []}
person = {"name": "John", "age": 23, "skils": skils}
person_datails = {"sex": "Male", "address": address}

######################### описание структуры данных с помощью словарей

person = {"name": "John",
          "age": 23,
          "sex": "Male",
          "address": {"city": "Dnipro",
                      "street": "Polya",
                      "ZIP": 49000
                      },
          "skils": {"hard": ["python", "html", "DB", "C++"],
                    "soft": []
                    }
          }

######################################### конструирование словаря через метод update
new_person = dict()
new_person.update(person)
new_person.update(person_datails)

new_person = {**person_datails, **person}
print(new_person["address"]["city"])
new_person["skils"]["hard"].append("JS")
print(new_person)
person.update(person_datails)
print(person)
person["sex"] = "Male"
print(person)

######################################## приведение к типу dict
my_tuple = (("name", "John"), ("age", 23))
my_list = [("name", "John"), ["age", 23]]
person = dict(my_list)
print(person)


########################################## циклы и dict

my_dict = {1: 11, (1, 2, 3): "test", "1": "TEST"}
print(11 in my_dict)  # in  "смотрит" только в ключи

print(my_dict.keys())  # dict_keys - "почти" список ключей ))
keys = list(my_dict.keys())
values = my_dict.values()   #dict_values - "почти" список значений
items = my_dict.items()
print(items)


my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}

for key in my_dict:  # "идет" ТОЛЬКО ПО КЛЮЧАМ
    print(key, my_dict[key])

res_values = []
res_keys = []
for key, value in my_dict.items():
    if value > 10:
        res_values.append(value)
        res_keys.append(key)

print(res_values)
print(res_keys)