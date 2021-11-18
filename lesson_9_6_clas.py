# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
from string import ascii_lowercase as alphabet
from random import shuffle


class AlphabetWorker:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.crate_folder()

    def crate_folder(self):
        os.makedirs(self.dir_name, exist_ok=True)

    def create_file(self, symbol):
        filename = f"{symbol}.txt"
        with open(f"{self.dir_name}/{filename}", "w") as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def create_alphabet_files(self):
        for symbol in alphabet:
            self.create_file(symbol)

    def do_tanos_click(self):
        files = os.listdir(self.dir_name)
        shuffle(files)
        for filename in files[:len(files) // 2]:
            os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet3"
alphabet_worker = AlphabetWorker(dir_name)
alphabet_worker.create_alphabet_files()
alphabet_worker.do_tanos_click()

# crate_folder(dir_name)
# create_alphabet_files(dir_name)
# do_tanos_click(dir_name)