# Interpolação básica de strings
# s - strings
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF123456789)

nome = 'Luiz'
preco = 1000.948923454
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))
