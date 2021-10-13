# 1
number = 15920065950598684500286
str_number = str(number)
zero_count = str_number.count('0')
print(zero_count)
##############################################################
# 2
number = 1502000000000
str_number = str(number)
zero_count = len(str_number) - len(str_number.rstrip('0'))
print(zero_count)
##############################################################
# 3
my_str = '95 больше чем 65 но меньше чем 99'
sum_numbers = sum([int(element) for element in my_str.split() if element.isdigit()])
print(sum_numbers)
##############################################################
# 4
my_str = 'Halloween is comiiieing.'
l_limit = 'l'
r_limit = 'i'
sub_str = my_str[my_str.find(l_limit) + 1 : my_str.rfind(r_limit)]
print(sub_str)
##############################################################
# 5
my_list = ['lemon', 'apple', 'peach', 'apricot', 'banana', 'raspberries', 'avocado']
new_list = [fruit for fruit in my_list if fruit.startswith('a')]
print(new_list)
##############################################################
# 6
my_list = ['lemon', 'apple', 'peach', 'apricot', 'banana', 'coconut', 'avocado']
new_list = [fruit for fruit in my_list if 'a' in fruit]
print(new_list)
##############################################################
# 7
my_list = [16, '8', '2', 3, 24, '65', '33', 5, '13', '121']
new_list = [value for value in my_list if value is str(value)]
print(new_list)
##############################################################
#8
my_str = 'ksb9iufw1wuhfu5'
new_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
print(new_list)
##############################################################
#9
my_str_1 = 'vnduoghsdfjg'
my_str_2 = 'nlojbfwojg'
my_list = list(set(my_str_1).intersection(set(my_str_2)))
print(my_list)
##############################################################
# 10
my_str_1 = 'vnduouughad'
my_str_2 = 'nojvaojgo'
my_list_1 = [sym_1 for sym_1 in my_str_1 if my_str_1.count(sym_1) == 1]
my_list_2 = [sym_2 for sym_2 in my_str_2 if my_str_2.count(sym_2) == 1]
result_list = list(set(my_list_1).intersection(set(my_list_2)))
print(result_list)
##############################################################
# 11
my_str = 'zvcvb1nmasdfg5hjklqwertyi'
my_list = []
for index in range(0, len(my_str), 2):
    if index % 2 == 0:
        part = my_str[index:index + 2]
        if len(part) > 1:
            my_list.append(part)
        else:
            my_list.append(part + '_')
print(my_list)
