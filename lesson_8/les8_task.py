import datetime
import json
import argparse
import requests


def values_valid(args) -> object:
    with open('symbols.json', 'r') as f:
        symbols_f = json.load(f)
        curr_list = [symbols for symbols in symbols_f['symbols']]
    currency_from = args.currency_from
    if currency_from.upper() not in curr_list:
        print('curr_from not in list')
        currency_from = 'USD'
    currency_to = args.currency_to
    if currency_to.upper() not in curr_list:
        print('curr_to not in list')
        currency_to = 'UAH'
    try:
        amount = float(args.amount)
    except ValueError:
        amount = 100.00
    try:
        if args.start_date is not None:
            start_date = datetime.datetime.strptime(input(args.start_date, '%Y-%n-%d'))
            if start_date > datetime.datetime.now():
                start_date = datetime.datetime.now()
        else:
            start_date = datetime.datetime.now()
    except ValueError:
        start_date = datetime.datetime.now()
    return convert(currency_from, currency_to, amount, start_date)


def convert(currency_from, currency_to, amount, start_date):
    while start_date <= datetime.datetime.now():
        request = requests.get('https://api.exchangerate.host/convert?',
                               params={'from': currency_from, 'to': currency_to,
                                       'amount': amount, 'date': start_date})
        data = request.json()
        print(data['date'],
              data['query']['from'],
              data['query']['to'],
              data['query']['amount'],
              data['info']['rate'],
              data['result'])
        start_date += datetime.timedelta(days=5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exchange rates')
    parser.add_argument('currency_from')
    parser.add_argument('currency_to')
    parser.add_argument('amount')
    parser.add_argument('--start_date')
    args = parser.parse_args()
    values_valid(args)
