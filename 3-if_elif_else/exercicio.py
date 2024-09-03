primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

if primeiro_valor < segundo_valor:
    print(f'{primeiro_valor=} é menor que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
