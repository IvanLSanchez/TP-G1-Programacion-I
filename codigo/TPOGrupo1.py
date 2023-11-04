# filtrarEntradasPorTitulo-maximoDiccionario-porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
## filtrarEntradasPorAño - maximoDiccionario
###
####
#####
######

# Funciones lambda
## item 1, 2
reglasTresSimples = lambda x,y,z: (x*y)/z    #Porcentaje, x=maximo, y=100, z= el total
maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda item: item[1]) #Devuelve la tupla con el valor maximo en factor de la clave

## item 4
ordenarDiccionarioPorKey = lambda diccionario: dict(sorted(diccionario.items(), key=lambda item: item[0])) #Ordena un diccionario en funcion de las claves

# Funciones
## item 1, 4
def filtrarEntradasPorTitulo(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por titulo, sin importar el periodo"""
    dic={}
    for linea in arch:
        nombre, año, sala=linea.split(";") #Desempaquetado de datos
        dic[nombre]=dic.get(nombre,0) + 1 #agrega y acumula
    return dic 

## item 2
def filtrarEntradasPorAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño

## item 4
def imprimirDiccionarioBase (diccionario, ancho, tituloColumnas):
    """imprime un diccionario base (key, value de 1 dato)
    para hacerlo necesita el ancho que ocupara y los titulos para los dos encabezados"""
    print("-".center(ancho,"-"))
    for titulo in tituloColumnas:
        print(titulo.center(ancho//2),end="")
    print()
    print("-".center(ancho,"-"))
    for key,value in diccionario.items():
        print(key.center(ancho//2), end="")
        print(str(value).center(ancho//2))
        print("-".center(ancho,"-"))
    

#=========================================================================================================

try:
    baseDeDatos = open("codigo/basesDeDatos/peliculas.txt","rt")
    entradasTitulo = filtrarEntradasPorTitulo(baseDeDatos)
    entradasTitulo = ordenarDiccionarioPorKey(entradasTitulo)
    imprimirDiccionarioBase(entradasTitulo, 100, ["Titulo","cantidad de Entradas"])
except OSError:
    print("error al abrir aechivo")
finally:
    try:
        baseDeDatos.close()
    except:
        pass