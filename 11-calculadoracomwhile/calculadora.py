while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro Número: ')
    operador = input('Digite o operador (+ - * /): ')

    num_validos = None

    try:
        num1_float = float(num1)
        num3_float = float(num2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break