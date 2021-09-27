# приведение типов
value_0 = False
value = str(value_0)
new_value = bool(value)
print(new_value, type(new_value))


# логический тип bool
some_value = 4
bool_value_1 = (2 == some_value)
bool_value_2 = ("z" not in "q.werty")
print(bool_value_2)


bool_value = bool_value_1 or bool_value_2
print(bool_value_1, bool_value_2, bool_value)
print(bool_value, type(bool_value))


# Математические действия
value_1 = "250"
value_2 = "3"

# value = value_1 / value_2  # обычное деление
# value = value_1 // value_2  # целочисленное деление (без округления)
# value = value_1 % value_2 # остаток от деления
# value = value_1 ** value_2  # возведение в степень. Корень для ** 0.5

value = value_1 + value_2
print(value) #, type(value))


# Переменные и типы в пайтон
value = '100'
# value = 100
print(value, type(value))

first = "qwe"
second = 1
value = first
first = second
second = value

first, second = second, first

print(first, second)

# Начало
print("Hello, World!")
# comment
print("Hello, World2") # sadkjfskdjhbvklsdhfkhvkszdfhvbkszbvkxbzdv
print('Hello!')

print(123 * 2, '456', "789", "qwe")  # PEP8
print(12 - 3)
print (23 + 5 * 10)