"""
Métodos úteis:
    append - adiciona um item final
    insert - adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga a lista
    extend - estende a lista
    + - concatena listas
Create Read Update    Delete
Criar, ler, Alterar   Apagar = lista[i] (CRUD)
"""

lista = [10,20,30,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1234)
del lista[-1]
lista.insert(0, 5)
print(lista)
