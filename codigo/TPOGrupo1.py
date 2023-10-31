#espectadoresAño - maximo

maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda x: x[1]) #Devuelve la tupla con el valor maximo en factor de la clave

def espectadoresAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño

#==================================================================================================
