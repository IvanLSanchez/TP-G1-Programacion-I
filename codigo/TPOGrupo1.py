# recopilacion-maximoDiccionario-porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
## espectadoresAño - maximo
###
####
#####
######

porcentaje = lambda x,y,z: (x*y)/z    #Porcentaje, x=maximo, y=100, z= el total

maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda x: x[1]) #Devuelve la tupla con el valor maximo en factor de la clave

def espectadoresAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño
  
def recopilacion(arch):
    """recopilacion y creacion del diccionario"""
    dic={}
    for linea in arch:
        nombre, año, sala=linea.split(";") #Desempaquetado de datos
        dic[nombre]=dic.get(nombre,0) + 1 #agrega y acumula
    return dic 
#=========================================================================================================