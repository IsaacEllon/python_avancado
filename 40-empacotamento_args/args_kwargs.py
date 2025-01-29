#Empacotamento e desempacotamento e dicionários

a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = { #dicionário
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa.items()
print(a, b)

# kwargs - keyword arguments (argumentos nomeados)