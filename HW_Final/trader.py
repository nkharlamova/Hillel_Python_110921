import argparse
import json
import csv
import os.path
from random import uniform


# функция № 1 ОБЯЗАТЕЛЬНАЯ проверяет на наличие файла history.csv, если его нет, то создает этот файл
def get_data(data, filename="system_history.csv"):
    if not os.path.isfile("system_history.csv"):
        with open(data, "r", encoding='utf-8') as file:
            read_file = json.load(file)
        with open(filename, 'w', encoding='utf-8') as file_csv:
            fieldnames = ["rate", "uah_count", "usd_count", "command"]
            writer = csv.DictWriter(file_csv, fieldnames=fieldnames, delimiter=",", lineterminator="\r")
            writer.writeheader()
            writer.writerow(
                {"rate": read_file["rate"], "uah_count": read_file["uah_count"], "usd_count": read_file["usd_count"],
                 "command": None})
    else:
        pass


# функция № 2 ОБЯЗАТЕЛЬНАЯ читает последнюю строку файла history.csv
def read_last_line(filename):
    results = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(row)
        last_history = results[-1]
    return last_history


# функция № 3 ОБЯЗАТЕЛЬНАЯ   записывает результат каждой специальной функции в файл history.csv
def write_data(data, command):
    data["command"] = command
    with open("system_history.csv", "a", newline='') as file:
        reader = csv.writer(file)
        data_val = list(data.values())
        reader.writerow(data_val)


# функция № 4 СПЕЦИАЛЬНАЯ  - Покупка доллара
def buy_usd(number, hist_dict):
    number = float(number)
    hist_dict["rate"] = float(hist_dict["rate"])
    hist_dict["uah_count"] = float(hist_dict["uah_count"])
    hist_dict["usd_count"] = float(hist_dict["usd_count"])
    if hist_dict["uah_count"] < (number * hist_dict["rate"]):
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {number * hist_dict['rate']}, AVAILABLE {hist_dict['uah_count']}")
        return hist_dict
    else:
        hist_dict["uah_count"] = round(hist_dict["uah_count"] - (number * hist_dict["rate"]), 2)
        hist_dict["usd_count"] = round(hist_dict["usd_count"] + number, 2)
        return hist_dict


# функция № 5 СПЕЦИАЛЬНАЯ - Продажа доллара
def sell_usd(number, hist_dict):
    number = float(number)
    hist_dict["rate"] = float(hist_dict["rate"])
    hist_dict["uah_count"] = float(hist_dict["uah_count"])
    hist_dict["usd_count"] = float(hist_dict["usd_count"])
    if hist_dict["usd_count"] < number:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {number}, AVAILABLE {hist_dict['usd_count']}")
        return hist_dict
    else:
        hist_dict["uah_count"] = round(hist_dict["uah_count"] + (number * hist_dict["rate"]), 2)
        hist_dict["usd_count"] = round(hist_dict["usd_count"] - number, 2)
        return hist_dict


# функция № 6 СПЕЦИАЛЬНАЯ - Покупка доллара на все гривны
def buy_all(hist_dict):
    hist_dict["rate"] = float(hist_dict["rate"])
    hist_dict["uah_count"] = float(hist_dict["uah_count"])
    hist_dict["usd_count"] = float(hist_dict["usd_count"])
    if hist_dict["uah_count"] == 0:
        print("You haven't money for buying USD.")
    else:
        hist_dict["usd_count"] = round((hist_dict["uah_count"] / hist_dict["rate"]) + hist_dict["usd_count"], 2)
        hist_dict["uah_count"] = round(hist_dict["uah_count"] - hist_dict["uah_count"], 2)
    return hist_dict


# функция № 7 СПЕЦИАЛЬНАЯ - Продажа всех долларов
def sell_all(hist_dict):
    hist_dict["rate"] = float(hist_dict["rate"])
    hist_dict["uah_count"] = float(hist_dict["uah_count"])
    hist_dict["usd_count"] = float(hist_dict["usd_count"])
    if hist_dict["usd_count"] == 0:
        print("You haven't money for selling USD.")
    else:
        hist_dict["uah_count"] = round((hist_dict["usd_count"] * hist_dict["rate"]) + hist_dict["uah_count"], 2)
        hist_dict["usd_count"] = round(hist_dict["usd_count"] - hist_dict["usd_count"], 2)
    return hist_dict


# функции № 8 - 9 СПЕЦИАЛЬНЫЕ - Получение дельты из config.json и формирование рандомного курса
# в пределах дельты
def get_delta(data):
    with open(data, "r", encoding='utf-8') as file:
        read_file = json.load(file)
        delta = read_file["delta"]
    return delta


def change_rate(hist_dict, config_delta):  # получаем рандомный курс
    hist_dict["rate"] = float(hist_dict["rate"])
    hist_dict["rate"] = round((uniform((hist_dict["rate"] - config_delta), (hist_dict["rate"] + config_delta))), 2)
    return hist_dict


# # функция № 10 СПЕЦИАЛЬНАЯ - Удаление файла состояния системы, программу можно запускать заново
def restart_program(filename):
    if os.path.isfile(filename):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        os.remove(path)
    else:
        pass


commands = argparse.ArgumentParser()
commands.add_argument("command", nargs="*", default="none", help="You can use only commands such as 'RATE', "
                                                                 "'AVAILABLE', 'BUY XXX' (USD), 'SELL XXX'(USD), "
                                                                 "'BUY ALL', 'SELL ALL',"
                                                                 "'NEXT', 'RESTART'.")
args = commands.parse_args()

if args.command == "none":
    print("COMMAND NOT DEFINED.")
elif args.command[0] == "RATE":
    get_data("config.json")
    last_operation_dict = read_last_line("system_history.csv")
    write_data(last_operation_dict, "RATE")
    print(f"CURRENT RATE {last_operation_dict['rate']}")
elif args.command[0] == "AVAILABLE":
    get_data("config.json")
    last_operation_dict = read_last_line("system_history.csv")
    write_data(last_operation_dict, "AVAILABLE")
    print(f"AVAILABLE BALANCE: {last_operation_dict['uah_count']} UAH, {last_operation_dict['usd_count']} USD")
elif args.command[0] == 'BUY' and len(args.command) == 1:
    print("USE 'BUY XXX' OR 'BUY ALL'")
elif args.command[0] == 'BUY' and args.command[1] != "ALL":
    if args.command[1].isdigit():
        get_data("config.json")
        last_operation_dict = read_last_line("system_history.csv")
        new_dict_buy = buy_usd(args.command[1], last_operation_dict)
        write_data(new_dict_buy, "BUY")
    else:
        print("NUMBER IS REQUIRED.")
elif args.command[0] == 'SELL' and len(args.command) == 1:
    print("USE 'SELL XXX' OR 'SELL ALL'")
elif args.command[0] == "SELL" and args.command[1] != "ALL":
    if args.command[1].isdigit():
        get_data("config.json")
        last_operation_dict = read_last_line("system_history.csv")
        new_dict_sell = sell_usd(args.command[1], last_operation_dict)
        write_data(new_dict_sell, "SELL")
    else:
        print("NUMBER IS REQUIRED.")
elif args.command[0] == "BUY" and args.command[1] == "ALL":
    get_data("config.json")
    last_operation_dict = read_last_line("system_history.csv")
    new_dict_buy_all = buy_all(last_operation_dict)
    write_data(new_dict_buy_all, "BUY_ALL")
elif args.command[0] == "SELL" and args.command[1] == "ALL":
    get_data("config.json")
    last_operation_dict = read_last_line("system_history.csv")
    new_dict_sell_all = sell_all(last_operation_dict)
    write_data(new_dict_sell_all, "SELL_ALL")
elif args.command[0] == "NEXT":
    get_data("config.json")

    last_operation_dict = read_last_line("system_history.csv")
    next_rate = change_rate(last_operation_dict, get_delta("config.json"))
    write_data(next_rate, "NEXT")
elif args.command[0] == "RESTART":
    restart_program("system_history.csv")
else:
    print("INCORRECT COMMAND.")