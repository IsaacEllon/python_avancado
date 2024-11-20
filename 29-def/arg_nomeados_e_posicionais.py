"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y):
    # Definição
    print(f'{x=} y={y}', '|', 'X + y =', x + y)

soma(y=2, x=3)

print(1, 2, 3, sep = ' - ')