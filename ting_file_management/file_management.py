import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido')

    try:
        with open(path_file) as file:
            result = [line.strip() for line in file.readlines()]
            return result
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
