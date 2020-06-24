def coger_digito(n):
    if n < 10:
        if n == 3 or n == 6 or n == 9:
            return [n] 
        else:
            return []      
    else:
        if n < 1000 and n > 100:
            if int((n % 1000 - n % 100)/100) == 3 or int((n % 1000 - n % 100)/100) == 6 or int((n % 1000 - n % 100)/100) == 9:
                if int((n % 100 - n % 10)/10) == 3 or int((n % 100 - n % 10)/10) == 6 or int((n % 100 - n % 10)/10) == 9:
                    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                        return [int((n % 1000 - n % 100)/100) , int((n % 100 - n % 10)/10), n % 10]
                    else:
                        return [int((n % 1000 - n % 100)/100) , int((n % 100 - n % 10)/10)]
                elif n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                    return [int((n % 1000 - n % 100)/100),n % 10]
            elif int((n % 100 - n % 10)/10) == 3 or int((n % 100 - n % 10)/10) == 6 or int((n % 100 - n % 10)/10) == 9:
                    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                        return [int((n % 100 - n % 10)/10), n % 10]
                    else:
                        return [int((n % 100 - n % 10)/10)]
            elif n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                return [n % 10]
            else:
                return []
                    
        elif n < 100 and n > 10:
            if int((n % 100 - n % 10)/10) == 3 or int((n % 100 - n % 10)/10) == 6 or int((n % 100 - n % 10)/10) == 9:
                if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                    return [int((n % 100 - n % 10)/10) , n % 10]
                else:
                    return [int((n % 100 - n % 10)/10)]
            elif n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
                return [n % 10]
        else:
            return []

def eliminar_vacios(lista):
    if lista == []:
        return []
    else:
        for i in range(len(lista)-1, -1, -1):
            if lista[i] == []:
                del lista[i]
        return lista



def lista_de_listas(lista):
    if lista == []:
        return []
    else:
        return [(coger_digito(a)) for a in lista]

print(eliminar_vacios(lista_de_listas([623,145,963,739,667,931,7,6])))
