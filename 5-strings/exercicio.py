nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}\n')
    print(f'Seu nome invertido é: {nome[::-1]}\n')

    if ' ' in nome:
        print(f'Seu nome contém espaços\n')
    else:
        print(f'Seu nome não contém espaços\n')

    print(f'Seu nome tem {len(nome)} letras\n')
    print(f'A primeira letra do seu nome é: {nome[0]}\n')
    print(f'A ultima letra do seu nome é: {nome[-1]}\n')
else:
    print('Desculpe você deixou espaços vazios.\n')