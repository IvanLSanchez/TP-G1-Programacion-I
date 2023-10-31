#FUNCIONES
## recopilacion-maximoDiccionario-porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
porcentaje = lambda x,y,z: (x*y)/z    #Porcentaje, x=maximo, y=100, z= el total 
maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda x: x[1]) #Maximo del diccionario
def recopilacion(arch):
    """recopilacion y creacion del diccionario"""
    dic={}
    for linea in arch:
        nombre, año, sala=linea.split(";") #Desempaquetado de datos
        dic[nombre]=dic.get(nombre,0) + 1 #agrega y acumula
    return dic 
        







