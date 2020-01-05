'''
Los sets son muy similares a las listas, pero estas no permiten elementos repetidos.

Cuando trabajamos con sets, podemos realizar las operaciones básicas de conjuntos,
esto quiere decir que se puede calcular los valores de intercepción, diferencia, unión.

'''

s = set([1, 2, 3])
t = set([3, 4, 5])

s.union(t) # set([1, 2, 3, 4, 5])
s.intersection(t) # set([3])
s.difference(t) # set([1, 2])
t.difference(s) # set([4, 5])

1 in s # True
5 in t # True
4 not in s # True
