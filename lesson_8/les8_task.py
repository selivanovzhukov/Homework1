import requests
import urllib.request
from pprint import pprint
import json
import datetime

with open('symbols.json', 'r') as f:
    f = json.load(f)

currency_from = str(input('Enter value: '))
for symbols in f:
    if currency_from not in symbols:
        print('curr_from incorrect, using default value')
        currency_from = 'USD'
currency_to = str(input('Enter value:'))
if currency_to not in f:
    print('curr_to incorrect, using default value')
    currency_to = 'UAH'
amount = float(input('enter:'))
if amount <= 0:
    amount = 100.00
start_date = str(input())

