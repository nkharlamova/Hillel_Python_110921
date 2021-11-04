import json
import re


# 1
def get_json_data(filename):
    with open(filename, "r", encoding='utf-8') as file:
        result = json.load(file)
    return result


# 2
def sort_by_surname(person_dict):
    surname = person_dict['name'].split()[-1]
    return surname


# 3
def sort_by_death_year(person_dict):
    years = person_dict['years']
    date_of_death = int(re.findall(r'[0-9]+', years)[-1])
    if 'BC' in years:
        date_of_death = -date_of_death
    return date_of_death


# 4
def sort_by_word_count(person_dict):
    word_count = len(person_dict['text'].split())
    return word_count


file_content = get_json_data('data.json')
print(file_content)

sort_person_by_name = sorted(file_content, key=sort_by_surname)
print(sort_person_by_name)

sort_person_by_date_of_death = sorted(file_content, key=sort_by_death_year)
print(sort_person_by_date_of_death)

sort_text_word_count = sorted(file_content, key=sort_by_word_count)
print(sort_text_word_count)
