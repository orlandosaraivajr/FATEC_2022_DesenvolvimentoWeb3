import pickle


if __name__ == "__main__":
    with open('registros.bin', 'rb') as list_in_file:
        registros = pickle.load(list_in_file)
