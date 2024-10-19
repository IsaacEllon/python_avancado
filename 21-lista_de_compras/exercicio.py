import os
lista_de_compras = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir  [a]pagar  [l]istar: ')
    os.system('cls')

    if opcao == 'i':
        inserir_valor = input('Valor: ')
        lista_de_compras.append(inserir_valor)

    elif opcao == 'a':
        apagar_valor = input('Qual produto deseja apagar? ')
        
        try:
            apagar_valor_int = int(apagar_valor)
            del lista_de_compras[apagar_valor_int]
        except ValueError:
            print('Por favor, Digite um número inteiro')
        except IndexError:
            print('Índice não existe')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        indices = range(len(lista_de_compras))
    
        if len(lista_de_compras) == 0:  
            print('Não tem nada para listar\n')

        for indice in indices:
            print(indice, lista_de_compras[indice])

    else:
        print('Escolha i, a ou l\n')