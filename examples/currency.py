#!/usr/bin/env python3

# Generated for you at: https://www.exchangerate-api.com/app/dashboard
import datetime

import requests

# ExchangeRate-API {
# - Un: lucassaporetti
# - Pw: 123gabiroba4
# }

# This is the security key used to access the site API.
API_KEY = "bb2beecc3cfa14b9e7856bab"

# Version of the API used on this program.
API_VERSION = 'v5'

# This is the url for the site to retrieve the conversion rates.
BASE_API_URL = f"https://prime.exchangerate-api.com/{API_VERSION}/"

# This object hold the possible conversions. Took those from the API response.
CURRENCIES = [
    "USD", "AED", "ARS", "AUD", "BGN", "BRL", "BSD",
    "CAD", "CHF", "CLP", "CNY", "COP", "CZK", "DKK",
    "DOP", "EGP", "EUR", "FJD", "GBP", "GTQ", "HKD",
    "HRK", "HUF", "IDR", "ILS", "INR", "ISK", "JPY",
    "KRW", "KZT", "MXN", "MYR", "NOK", "NZD",
    "PAB", "PEN", "PHP", "PKR", "PLN", "PYG", "RON",
    "RUB", "SAR", "SEK", "SGD", "THB", "TRY",
    "TWD", "UAH", "UYU", "ZAR"
]


def build_url(currency):
    return f'{BASE_API_URL}/{API_KEY}/latest/{currency}'


def get_conversions(currency):
    url = build_url(currency)
    print("Retrieving conversion from: " + url)
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f'##ERROR => Failed to retrieve conversion rates from server status={resp.status_code} !')
        return None


print('Select a conversion')
print('=' * 30)

from_currency = input('From [USD]: ')
from_currency = from_currency.upper() if from_currency else 'USD'
to_currency = input('To [BRL]: ')
to_currency = to_currency.upper() if to_currency else 'BRL'
amount = input('Amount [1]: ')
amount = int(amount if amount else '1')

if from_currency in CURRENCIES and to_currency in CURRENCIES:
    response = get_conversions(from_currency)
    update_time = datetime.datetime.fromtimestamp(
        response['time_last_update']).isoformat()
    print(f"Currency conversion {update_time} rates updated !")
    rates = response['conversion_rates']
    if rates is not None:
        converted_value = round(rates[to_currency]*amount, 2)
        print("Conversion {:3s} {:d} == {:3s} {:.2f}".format(
            from_currency, amount, to_currency, converted_value
        ))
else:
    print(f'##ERROR => Conversion not found: from {from_currency} to {to_currency} !')
