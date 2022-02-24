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
