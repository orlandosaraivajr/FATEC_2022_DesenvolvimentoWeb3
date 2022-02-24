import pickle


if __name__ == "__main__":
    with open('registros.bin', 'rb') as list_in_file:
        registros = pickle.load(list_in_file)


# Desafio 1: Capturar os nomes que começam com a letra "M"
# Solução 1

for registro in registros:
    if registro[0][0] == 'M':
        print(registro[0])

for registro in registros:
    if registro[0].startswith('M'):
        print(registro[0])

# Desafio 2: Capturar os registros com endereços do estado de SP
# e armazenar em uma lista chamada "estado_SP"

estado_SP = []
for registro in registros: 
    if registro[1][-2:] == 'SP': 
        estado_SP.append(registro) 

estado_SP = []    
for registro in registros: 
    if '/ SP' in registro[1]: 
        estado_SP.append(registro) 
    
estado_SP = []
for registro in registros: 
    if registro[1].endswith('SP'): 
        estado_SP.append(registro) 

# Desafio 3: Remover itens duplicados de uma lista

lista_mercado = ['Arroz', 'Feijão', 'Macarrão', 'Coca-cola']
lista_mercado += ['Arroz', 'Coca-cola', 'arroz', 'coca-cola']
lista_mercado += ['Arroz', 'Feijão', 'Macarrão', 'Coca-cola']
lista_mercado += ['Arroz', 'Coca-cola', 'arroz', 'coca-cola']

lista_mercado = list(set(lista_mercado))

numeros = set(range(1,10)) 
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros2 = set(range(5,15))
# {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
numeros2.intersection(numeros) 
# {5, 6, 7, 8, 9}
numeros.union(numeros2)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
numeros.difference(numeros2) 
# {1, 2, 3, 4}
numeros.symmetric_difference(numeros2)  
# {1, 2, 3, 4, 10, 11, 12, 13, 14}

