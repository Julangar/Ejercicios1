def coger_digito(n):
    if n < 10:
        return n
    else:
        return n % 10

def lista_digitos(lista):
    if lista == []:
        return []
    else:
        return [(str(coger_digito(n))) for n in lista]

def concat_elementos(lista):
	if lista == []:
		return ""
	else:
		return lista[0] + concat_elementos(lista[1:])

print(concat_elementos(lista_digitos([23,41,56])))
