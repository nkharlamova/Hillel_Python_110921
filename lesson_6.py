# параметры функций
# модуль os
# работа с файлами
# практическая работа

#######################################################

with open("HW/lesson4.txt", "r") as file:
    # data = file.read()  # считал все одной строкой
    data = file.readlines()
print(data)

file = open("HW/lesson4.txt", "r")
data = file.read()
file.close()

data.append('TEST\n')

with open("HW/lesson4_test.txt", "w") as txt_file:
    txt_file.writelines(data)


########################################################
import os

dir = os.listdir("HW")
print(dir)

filename = 'lesson3.txt'
folder = "HW"
path = f"{folder}/{filename}"
path = os.path.join(os.getcwd(), folder, filename)
print(path)
os.mkdir("test/test2") ## не рекомендую ))
os.makedirs("test1/test3", exist_ok=True)  # !!!!!

for filename in sorted(dir):
    file_path = os.path.join("HW", filename)
    if os.path.isfile(file_path):
        print(f"{filename=}")


#########################################################
def test_func(par_1: str, par_2: str, par_3: str, par_4: str = "asdfgh") -> int:
    return len(f"{len(par_1)}_{len(par_2)}_{len(par_3)}_{len(par_4)}")

def test_func_2(*args, **kwargs):
    print(args)
    print(kwargs)


print(test_func_2("John", 24, job="programmer", animal="dog"))

#########################################################
from random import randint

MIN_LIMIT = 1
MAX_LIMIT = 10


triangle_abc = {"A": (2, 3),
                "B": (-4, 7),
                "C": (0, 0)}

def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    return (randint(min_limit, max_limit), randint(min_limit, max_limit))


def create_triangle(min_limit, max_limit):
    triangle_dict = {"A": create_point(min_limit, max_limit),  # DRY
                     "B": create_point(min_limit, max_limit),
                     "C": create_point(min_limit, max_limit)}
    return triangle_dict

# def create_triangle(name="ABC"):
#     triangle_dict = {name[0]: create_point(),  # DRY
#                      name[1]: create_point(),
#                      name[2]: create_point()}
#     return triangle_dict


def create_triangles_list(number=3):
    return [create_triangle("QWE") for _ in range(number)]


# triangle_abc = create_triangle()
print(triangle_abc)

triangles_list = create_triangles_list(5)
print(triangles_list)