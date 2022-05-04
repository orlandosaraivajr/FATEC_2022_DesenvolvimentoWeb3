import requests 
URL = 'https://pokeapi.co/api/v2/ability/' 
req = requests.get(URL)
dados_recebidos = req.json() 
lista = []
for habilidade in dados_recebidos['results']:
    lista.append((habilidade['name'], habilidade['url']))
