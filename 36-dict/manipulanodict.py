# MAnipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Isaac'
pessoa['sobrenome'] = 'Ellon'


print(pessoa[chave])

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])