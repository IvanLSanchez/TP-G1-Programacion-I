# recopilacion-maximoDiccionario-porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
## espectadoresAño - maximo
###
####
#####
######

reglasTresSimples = lambda x,y,z: (x*y)/z    #Porcentaje, x=maximo, y=100, z= el total

maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda item: item[1]) #Devuelve la tupla con el valor maximo en factor de la clave

ordenarDiccionarioPorKey = lambda diccionario: sorted(diccionario.items(), key=lambda item: item[1]) #Ordena un diccionario en funcion de las claves

def filtrarEntradasPorAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño
  
def filtrarEntradasPorTitulo(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por titulo, sin importar el periodo"""
    dic={}
    for linea in arch:
        nombre, año, sala=linea.split(";") #Desempaquetado de datos
        dic[nombre]=dic.get(nombre,0) + 1 #agrega y acumula
    return dic 
#=========================================================================================================
