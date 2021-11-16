import re


def read_from_logs(filename):
    with open(filename, 'r') as file:
        data = file.read().split("\n")
    return data


def get_data(logs, mask):
    data = []
    for line in logs:
        res_line = re.findall(mask, line)
        data += res_line
    return data


logs = read_from_logs("logs.txt")
ip_mask = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
date_mask = r"\d{4}[-/]{1}\d{2}[-/]{1}\d{2}"
time_mask = r"\d{2}[:]{1}\d{2}[:]{1}\d{2}"

ips = get_data(logs, ip_mask)
print(ips)

dates = get_data(logs, date_mask)
print(dates)

times = get_data(logs, time_mask)
print(times)

