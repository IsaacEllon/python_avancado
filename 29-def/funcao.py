"""
Introdução às funções (def) e, Python
Funções são trechos de códigos usados para
replicar deterinada ação ao longo do código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, fnções Python retornam None (nada). 
"""

# def python():   
#    print('Várias')
#
#python()


#def imprimir(a, b, c):
#    print(a, b, c)

#imprimir(3, 6, 9)


def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao()