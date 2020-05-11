import requests as req
import sys
import json

request = req.get('https://economia.awesomeapi.com.br/json/all')
cotacoes = json.loads(request.text)

def exibeCotacoes(querys):
   global cotacoes

   keySet = cotacoes.keys()

   for query in querys:
      if(query in keySet):
         preco = (float(cotacoes[query]['high']) + float(cotacoes[query]['low']))/2
         preco = format(preco, '.2f')
         print(f"{preco} {cotacoes[query]['code']} / {cotacoes[query]['create_date']}")

consultas = ["USD", "ARS", "EUR", "BTC"]
if(len(sys.argv) > 1):
   consultas = sys.argv[1:]

print("1 BRL ==")
exibeCotacoes(consultas)
