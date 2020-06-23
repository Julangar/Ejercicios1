class Nodo():
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def coger_digito(n):
    if n < 10:
        return n
    else:
        return [coger_digito(int(n / 10)) , n % 10 ]

def lista_ordenada(lista):
    if lista == []:
        return []
    else:
        return [(coger_digito(n)) for n in lista]

arbol = Nodo(25,Nodo(15,None,Nodo(20)),Nodo(50,Nodo(55)))
print(en_orden(arbol))
print(lista_ordenada(en_orden(arbol)))