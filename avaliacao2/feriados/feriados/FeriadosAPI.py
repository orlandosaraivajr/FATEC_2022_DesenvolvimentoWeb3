import requests


class FeriadoAPI:
    def __init__(self, ano=2022):
        self._ano = ano
        self.feriados = []
        URL = 'https://brasilapi.com.br/api/feriados/v1/' + self.ano
        req = requests.get(URL)
        if req.ok:
            feriados = req.json()
            for feriado in feriados:
                tupla = (feriado.get('name'), feriado.get('date'))
                self.feriados.append(tupla)

    @property
    def ano(self):
        return str(self._ano)

    def __str__(self):
        return 'Feriados de ' + self.ano

    def __repr__(self):
        return str(self)
