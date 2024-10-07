frase = 'O python é uma linguagem de programação '\
    'multiparadigma' \
    'python foi criado por Guido Van Rossum'

print(frase.count('python')) # count - verifica quantas vezes o caractere a aparece. 

i = 0 
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1