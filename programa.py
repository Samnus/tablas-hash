import re
from prettytable import PrettyTable

def split(s, delimiter):
    return s.split(delimiter)

def process_input(input_text):
    hash_table = {}
    lines = input_text.split('\n')
    for row, line in enumerate(lines):
        tokens = split(line, ' ')
        col = 0
        for token in tokens:
            if token:
                key = f"{row},{col}"
                hash_table[key] = {'token': token, 'position': (row, col)}
                col += 1
    return hash_table

def print_hash_table(hash_table):
    table = PrettyTable()
    table.field_names = ["Clave", "Token"]
    for key, value in hash_table.items():
        table.add_row([key, value['token']])
    print(table)

def main():
    multiline_input = "int suma = 0;\nsuma = 54 + 20;"
    hash_table = process_input(multiline_input)

    while True:
        print("Bienvenido al programa de procesamiento de tokens en Python")
        print("Por favor elija una opción:")
        print("1. Visualizar tabla hash")
        print("2. Salir")
        choice = input("Ingrese su elección: ")

        if choice == '1':
            print("Tabla Hash:")
            print_hash_table(hash_table)
        elif choice == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
