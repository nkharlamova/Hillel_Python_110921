from random import randint, choice
from string import ascii_lowercase as alphabet


def change_list(my_list):
    for index in range(0, len(my_list), 2):
        my_list[index] = my_list[index][::-1]
    return my_list


def create_email(domains, names):
    name = choice(names)
    domain = choice(domains)
    number = randint(100, 999)
    my_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
    e_mail = f"{name}.{number}@{my_str}.{domain}"
    return e_mail

print(f"{__name__=}")

if __name__ == "__main__":
    my_list = ["qwe", "asd", "zxc", "123"]
    my_list = change_list(my_list)
    print("..............", my_list)

    names = ["king", "miller", "kean"]
    domains = ["net", "com", "ua"]
    e_mail = create_email(domains, names)
    print("----------->>>", e_mail)