import requests
import csv


### 1
def get_raw_quote(number):
    result_list = []
    key = 0
    while len(result_list) < number:
        params = {'method': 'getQuote',
                  'format': 'json',
                  'key': key,
                  'lang': 'ru'}
        quote = (requests.get(url, params=params)).json()
        key += 1
        if quote['quoteAuthor'] != '':
            try:
                result_list.append(quote)
            except Exception:
                pass
    return result_list


### 2
def create_quotes_csv_file(data, filename="quotes.csv"):
    data_list = []
    for every_dict in data:
        data_list.append([every_dict['quoteAuthor'], every_dict['quoteText'], every_dict['quoteLink']])

    with open(filename, 'w', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv, delimiter=",", lineterminator="\r")
        writer.writerow(['Author', 'Quote', 'URL'])
        writer.writerows(sorted(data_list, key=lambda x: x[0].lower()))


url = "http://api.forismatic.com/api/1.0/"
quotes_raw_list = get_raw_quote(20)
create_quotes_csv_file(quotes_raw_list)

