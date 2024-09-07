# Introdução ao try/except
# try -> tenta executar o código
# except -> ocorreu algum erro ao tentar executar
# isdigit - verifica se tem apenas int

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é uma número')