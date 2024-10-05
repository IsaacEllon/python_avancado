while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro Número: ')
    operador = input('Digite o operador (+ - * /): ')

    num_validos = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
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

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num1_float} + {num2_float} =', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} =', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} =', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} =', num1_float / num2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break