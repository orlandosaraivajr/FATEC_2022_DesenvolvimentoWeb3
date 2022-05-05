import requests

class PokemonService:
    
    def __init__(self):
        self.URL_BASE = 'https://pokeapi.co/'
        self.URL = self.URL_BASE + '/api/v2/'
    
    def lista_pokemons(self):
        lista_nomes = []
        for numero in range(1, 10):
            URL = self.URL + 'pokemon/' + str(numero)
            req = requests.get(URL)
            dados_recebidos = req.json()
            # import ipdb ; ipdb.set_trace()
            nome_pokemon = dados_recebidos['name']
            lista_nomes.append((numero, nome_pokemon))
        return lista_nomes
    
    def dados_pokemon(self, id):
        URL = self.URL + 'pokemon/' + str(id)
        req = requests.get(URL)
        dados_recebidos = req.json()
        nome_pokemon = dados_recebidos['name']
        lista_types = []
        for type in dados_recebidos['types']:
            lista_types.append(type['type']['name'])
        return (nome_pokemon, lista_types)
    
    def __str__(self):
        return 'Serviço Pokemon'
    
    def __repr__(self):
        return str(self)

service = PokemonService()