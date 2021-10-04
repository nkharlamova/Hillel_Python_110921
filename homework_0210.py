# задача № 1
my_list = [25, 18, 102, 13, 56, 545, 398, 24, 188, 17, 161, 222]
for number in my_list:
    if number > 100:
        print(number)
################################################################
# задача № 2
my_list = [25, 18, 102, 13, 56, 545, 398, 24, 188, 17, 161, 222]
my_results = []
for number in my_list:
    if number > 100:
        my_results.append(number)
print(my_results)
################################################################
# задача № 3
my_list = [25, 18, 102, 13, 56, 545, 398, 24, 188, 17, 161, 222]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)
################################################################
# задача № 4
my_string = "0123456789"
my_string_2 = my_string
int_list = []
for symb in my_string:
    for symb_2 in my_string_2:
        int_list.append(int(symb + symb_2))
print(int_list, type(int_list[3]), type(int_list))  # проверка
