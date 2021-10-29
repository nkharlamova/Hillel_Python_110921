## 1
def get_domains(filename):
    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            if line.startswith('.'):
                result.append(line.strip()[1:])
            else:
                result.append(line)  # на случай если где-то пропущена точка
        return result


domains_list = get_domains('domains.txt')
print(domains_list)


## 2
def get_names(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            result.append(line.split('\t')[1])
    return result


names_list = get_names('names.txt')
print(names_list)

## 3
from datetime import datetime


def get_dates(filename):
    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            one_line = line.split(" - ")
            if len(one_line) > 1:
                date_original = one_line[0]
                day, month, year = date_original.split()
                date_modified = datetime.strptime(f'{day[:-2]} {month} {year}', '%d %B %Y')
                result.append(
                    {
                        'date_original': date_original,
                        'date_modified': datetime.strftime(date_modified, '%d/%m/%Y')
                    }
                )
    return result


dates_list = get_dates("authors.txt")
print(dates_list)
