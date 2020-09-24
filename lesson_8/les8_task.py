import requests
import urllib.request
from pprint import pprint
import json
import datetime

with open('symbols.json', 'r') as f:
    symbols = json.load(f)

currency_from = str(input('Enter value: '))
for currency_from in symbols['symbols']:
    if currency_from not in symbols:
        print('curr_from incorrect, using default value')
        currency_from = 'USD'
currency_to = str(input('Enter value:'))
for currency_to in symbols['symbols']:
    if currency_to not in symbols:
        print('curr_to incorrect, using default value')
        currency_to = 'UAH'
amount = float(input('enter:'))
if amount <= 0:
    amount = 100.00
start_date = str(input())

