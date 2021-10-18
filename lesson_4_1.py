"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
Пример:  my_str="blablacar", my_symbol="bla".
Вывод на экран:
2
"""
my_str = "blablacarblablacar"
my_symbol="bla"

result = my_str.count(my_symbol)
# new_str = my_str.replace(my_symbol, '')
# result = (len(my_str) - len(new_str)) // len(my_symbol)
print(result)


"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
my_str = "blablacar"
my_symbol="bla"

my_symbol_count = my_str.count(my_symbol)

result = f"{my_symbol}\n" * my_symbol_count
result = result.strip()
print(result)

for _ in range(my_symbol_count):
    print(my_symbol)


"""
3) У вас есть переменная my_str, тип - str. 
Большая и маленькая буква считается как один символ.
Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.  
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
lower_str = my_str.lower()
unique_symbols = []

for symbol in lower_str:
    if symbol not in unique_symbols:
        unique_symbols.append(symbol)
unique_symbols_count = len(unique_symbols)
print(unique_symbols_count)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
val_1 = 123
val_2 = 100
val_1 += val_2
print(val_1)

my_str = "xdkzkzjdvkzsdbvkxbzvkhbdzsfh"
my_list = []
print(id(my_list), my_list)
new_str = my_str[::2]
# for symbol in new_str:
#     my_list.append(symbol)
my_list += list(new_str)  # НЕ ТО ЖЕ САМОЕ, ЧТО my_list = my_list + list(new_str)
print(id(my_list), my_list)
"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
from string import ascii_lowercase as alphabet

my_str = alphabet
str_index = [7, 8, 11, 11, 4, 11]
my_list = []
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
print(my_list)

"""
6)
Дано целое число (тип int). Определить сколько цифр в этом числе.
"""

number = 128973816581735168456287359129834092876582634
digit_count = len(str(number))
print(digit_count)


"""
7)
Дано целое число (тип int). Определить наибольшую цифру в этом числе.
"""
number = 2873816581735168456287351283402876582634
max_symbol = max(str(number))
print(max_symbol)


"""
8)
Дано целое число (тип int). Составить число (int) с цифрами в обратном порядке.
"""
number = 2873816581735168456287351283402876582634

# result_number = int(str(number)[::-1])

numb_str = str(number)
numb_str = numb_str[::-1]
result_number = int(numb_str)

print(result_number)

"""
9)
Дано целое число (тип int). Составить число с цифрами в порядке возрастания(убывания).
"""
number = 28738165817351684562873512834028765826340000000
numb_str = str(number)
sort_numb_list = sorted(numb_str, reverse=True)
new_number = "".join(sort_numb_list)
result = int(new_number)
print(result)


my_list = [3, 6, 1, 8]
# my_list_sorted = sorted(my_list, reverse=True)
my_list.sort(reverse=True)
print(my_list)



"""
10) Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и
my_list_2 через один, начиная с my_list_1.
а) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30]
my_result = []

for index in range(len(my_list_1)):
    # my_result.extend([my_list_1[index], my_list_2[index]])
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
print(my_result)

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = [10, 20, 30, 40, 50]
my_result = []

min_len_lists = min(len(my_list_1), len(my_list_2))
tail = my_list_1[min_len_lists:] + my_list_2[min_len_lists:]
print(tail)
for index in range(min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
my_result.extend(tail)
print(my_result)