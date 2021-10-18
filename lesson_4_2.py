# ord(), chr()
print(ord("A"))
print(chr(34))


# Генераторы списков (list comprehension)
alphabet_list = []
for index_ascii in range(ord('a'), ord('z') + 1):
    alphabet_list.append(chr(index_ascii))

alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') + 1)]
alphabet = "".join(alphabet_list)
print(alphabet)

result = [x ** 2 for x in range(25)]
print(result)

my_list = [12, -45, 23, 5, 0, 21, 900]

res = [str(value) * 20 for value in my_list if value > 10]
res = []
for value in my_list:
    if value > 10:
        res.append(value)

[print(line) for line in res]
for line in res:
    print(line)


# множества (set) - изменяемый тип, только один представитель для какждого объекта, порядок не сохраняется

my_list = [1, "2", 3, 4, "5", "5", "1"]
my_list_unique = list(set(my_list))  # Убрать дубли в списке
my_set = set(my_list)
my_set.add(1000)
print(my_set, type(my_set))


my_str = "bla BLA carqqqq"
unique_symbols_count = len(set(my_str.lower()))
print(unique_symbols_count)

my_str_1 = "sdlkjfgkzdfkzhdfkjvakjdfvbaydsgfaksjdasudvb"
my_str_2 = "saudhflsdkzao;uh giy7gfsazhnvcahirhvsmcflaouewyhflia"

my_str_1_set = set(my_str_1)
my_str_2_set = set(my_str_2)

same_symbols = my_str_1_set.intersection(my_str_2_set)
print(same_symbols)

all_symbols = my_str_1_set.union(my_str_2_set)
print(all_symbols)

first_str_unique = my_str_1_set.difference(my_str_2_set)
print(first_str_unique)