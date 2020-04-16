import datetime
date_string = input('A date: ')
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print(date_obj)
except ValueError:
  print("Incorrect data format, should be YYYY-MM-DD")

from datetime import date#escopo de importação

ano_atual = date.today().year
idade = ano_atual - a