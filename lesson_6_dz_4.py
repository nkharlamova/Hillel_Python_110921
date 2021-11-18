# 1. Дано целое число (int). Определить сколько нулей в этом числе.
number = 213490323020023470000
zero_count = str(number).count("0")
print(zero_count)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

zero_count_last_symbols = len(str(number)) - len(str(number).strip('0'))
print(zero_count_last_symbols)

# 3. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

test_str = "43 больше чем 34 но меньше чем 56"

numb_list = []
for word in test_str.split():
    if word.isdigit():
        numb_list.append(int(word))
result = sum(numb_list)
# result = sum([int(word) for word in test_str.split() if word.isdigit()])
print(result)

# 4. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
res_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(res_str)

# 5. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ["uyf", "asygfa", "sidfa", "a8732456"]
new_list = []
for my_str in my_list:
    if 'a' == my_str[0]:
        new_list.append(my_str)
print(new_list)

# 6. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["uyf", "asygfa", "sidfa", "a8732456"]
new_list = []
for my_str in my_list:
    if 'a' in my_str:
        new_list.append(my_str)
print(new_list)

# 7. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)

# 8. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = "sssssssssssssssssssssssssssssssssssssssdfafafnkajshfkajsdfgjhgam,vc"
res_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)

# 9. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "akjsgfasc.kahscauzsckasc"
my_str_2 = "aksudhanmmsjskasla;a"
res_list = list(set(my_str_1).intersection(set(my_str_2)))
print(res_list)

# 10. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdf1"
my_str_2 = "asdfff2"
res_list = []
for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)

# 11. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = "sakdhfashah"

if len(my_str) % 2:
    my_str += "_"
res_list = []
for index in range(0, len(my_str), 2):
    res_list.append(my_str[index: index + 2])

# my_str = my_str + "_" if len(my_str) % 2 else my_str
# res_list = [my_str[index: index + 2] for index in range(0, len(my_str), 2)]

print(res_list)