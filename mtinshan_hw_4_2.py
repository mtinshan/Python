import requests
from decimal import *
from datetime import datetime

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in response:
        return None
    inrub = response[(response.find('<Value>', response.find(val)) + 7)
                   :response.find('</Value>', response.find(val))]
    data_now = response[(response.find('Date="') + 6)
                        :response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, data_now)
    return f"{Decimal(inrub.replace(',', '.'))} RUB, {datetime(day=day, month=month, year=year)}"

print(currency_rates(input('Введите код валюты: ')))