nome = 'Otávio'
#print(nome[2])

print('vio' in nome) #Verifica se 'vio' está entre as letras da var nome
print('z' in nome)
print(10* '-')
print('vio' not in nome)
print('z' not in nome)


nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')