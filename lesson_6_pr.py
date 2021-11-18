# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet
from random import shuffle


def crate_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def create_file(symbol, folder_name):
    filename = f"{symbol}.txt"
    with open(f"{folder_name}/{filename}", "w") as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))


def create_alphabet_files(folder_name):
    for symbol in alphabet:
        create_file(symbol, folder_name)


def do_tanos_click(dir_name):
    files = os.listdir(dir_name)
    shuffle(files)
    for filename in files[:len(files) // 2]:
        os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet"
crate_folder(dir_name)
create_alphabet_files(dir_name)
do_tanos_click(dir_name)