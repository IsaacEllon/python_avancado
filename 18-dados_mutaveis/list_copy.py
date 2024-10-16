"""
Cuidados com os dados mutáveis
    = - copiado o vlor (imutáveis)
    = - aponta para o mesmo valor na memo´ria (mutável)
"""
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)