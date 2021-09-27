# 1
value = 625
new_value = value // 2 if value < 100 else - value
print(new_value)
##################################################################
# 2
value = 101
new_value = 1 if value < 100 else 0
print(new_value)
###################################################################
# 3
value = 550
new_value = True if value < 100 else False
print(new_value)
####################################################################
# 4
my_str = ('have a nice day!')
print(my_str.upper())
####################################################################
# 5
my_str = ('HAVE A NICE DAY!')
print(my_str.lower())
####################################################################
# 6
my_str = ('Good')
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)
####################################################################
# 7
my_str = ('Good')
if len(my_str) < 5:
    print(my_str + my_str[::-1])
else:
    print(my_str)
