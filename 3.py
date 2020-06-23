def mayor(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] > lista[1]:
			return mayor([lista[0]]+lista[2:])
		else:
			return mayor(lista[1:])

def mayores(lista):
	return [mayor(i) for i in lista]

def menor(lista):
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[0] < lista[1]:
			return menor([lista[0]]+lista[2:])
		else:
			return menor(lista[1:])

def menores(lista):
	return [menor(i) for i in lista]

def sumar_may_men(lista1, lista2):
    if lista1 == [] and lista2 == []:
        return []
    else:
        return [a+b for (a, b) in zip(lista1, lista2)]

def unir(lista1,lista2,lista3):
    if lista1 == [] and lista2 == [] and lista3 == []:
        return []
    else:
        return [(a,b,c) for (a, b, c) in zip(lista1, lista2, lista3)]

print(mayores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]))
print(menores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]))
print(sumar_may_men(mayores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]),menores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]])))
print(unir(mayores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]),menores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]),sumar_may_men(mayores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]),menores([[1,2,3],[4,5,6],[8,7,4],[2,10,4,9]]))))