"""
Lista em Python
Tipo list - mutável # list é = array do javascript
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamentos
Métodos úteis: 
    append, insert, pop, del, clear, extend, +

Create Read Uptade   Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)