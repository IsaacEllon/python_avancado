lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))

for item in lista_enumerada:
    indice, nome = item
    print (indice, nome)
    
