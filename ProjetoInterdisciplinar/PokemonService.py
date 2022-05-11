import requests
import logging

class PokemonService:
    
    def __init__(self):
        self.URL_BASE = 'https://pokeapi.co/'
        self.URL = self.URL_BASE + '/api/v2/'
        logging.basicConfig(filename='pokemon.log', level=logging.INFO)
    
    def lista_pokemons(self):
        lista_nomes = []
        for numero in range(1, 1000):
            URL = self.URL + 'pokemon/' + str(numero)
            req = requests.get(URL)
            if not req.ok:
                return lista_nomes
            dados_recebidos = req.json()
            nome_pokemon = dados_recebidos['name']
            logging.info(nome_pokemon) 
            lista_nomes.append((numero, nome_pokemon))
    
    def dados_pokemon(self, id):
        URL = self.URL + 'pokemon/' + str(id)
        req = requests.get(URL)
        dados_recebidos = req.json()
        nome_pokemon = dados_recebidos['name']
        lista_types = []
        logging.info('Método: dados_pokemon' + nome_pokemon) 

        for type in dados_recebidos['types']:
            lista_types.append(type['type']['name'])
        return (nome_pokemon, lista_types)
    
    def __str__(self):
        return 'Serviço Pokemon'
    
    def __repr__(self):
        return str(self)

service = PokemonService()