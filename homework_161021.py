## 1
persons = [
    {'name': 'Will', 'age': 13},
    {'name': 'William', 'age': 28},
    {'name': 'John', 'age': 13},
    {'name': 'Jillian', 'age': 45},
    {'name': 'Helen', 'age': 18}
]
# a
person_ages = []
person_names = []
for person in persons:
    person_ages.append(person['age'])
    person_names.append(person['name'])

for person in persons:
    if person['age'] == min(person_ages):
        print('the youngest person:', person['name'])
# б
max_len = max(len(name) for name in person_names)
for max_len_person in person_names:
    if len(max_len_person) == max_len:
        print('the longest name:', max_len_person)
# в
average_age = (sum(person_ages) / len(person_ages))
print('average age:', average_age)

## 2
my_dict_1 = {8: 99, 1: 11, 7: 55, 2: 29, 3: 33, 16: 28}
my_dict_2 = {4: 22, 2: 74, 5: 55, 1: 15, 17: 6, 8: 13, 19: 48}
# a
keys_1_list = list(my_dict_1.keys())
keys_2_list = list(my_dict_2.keys())
list_intersection = list(set(keys_1_list).intersection(set(keys_2_list)))
print(list_intersection)
# б
list_difference = list(set(keys_1_list).difference(set(keys_2_list)))
print(list_difference)
# в
new_dict_difference = {}
for key, value in my_dict_1.items():
    for number in list_difference:
        if number == key:
            couple_key_val = {key: value}
            new_dict_difference.update(couple_key_val)
print(new_dict_difference)
# г
new_dict = {**my_dict_1, **my_dict_2}
for key_1, value_1 in my_dict_1.items():
    for key_2, value_2 in my_dict_2.items():
        for number in list_intersection:
            if number == key_1 == key_2:
                couple_key_val = {key_1: [value_1, value_2]}
                new_dict.update(couple_key_val)
print(new_dict)

## 3
def reverse_second_string_in_list(some_list):
    result = []
    for index in range(len(some_list)):
        if index % 2:
            result.append(some_list[index][::-1])
        else:
            result.append(some_list[index])
    return result


my_list = ['test', 'some', 'list', 'now']
new_list = reverse_second_string_in_list(my_list)
print(new_list)

## 4
import random
import string


def create_email(domain, name):
    random_name = random.choice(names)
    random_domain = random.choice(domains)
    random_number = random.randint(100, 999)
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for letter in range(random.randint(5, 7)))
    result = str(random_name) + "." + str(random_number) + "@" + str(random_word) + "." + str(random_domain)
    return result


names = ['jameson', 'miller', 'kean', 'king', 'stivenson']
domains = ['net', 'com', 'ua', 'ru']
email = create_email(domains, names)
print(email)
