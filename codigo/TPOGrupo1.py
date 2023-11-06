# filtrarEntradasPorTitulo - maximoDiccionario - porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
## filtrarEntradasPorAño - maximoDiccionario
### espectadoresxSala - ordenarDiccionarioPorKey - imprimirTabla3ColumnasDict
#### filtrarEntradasPorTitulo - ordenarDiccionarioPorKey - imprimirTabla2ColumnasDict
#####
######

# Funciones lambda
## item 1, 2
reglasTresSimples = lambda x,y,z: (x*y)/z    #Porcentaje, x=maximo, y=100, z= el total
maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda item: item[1]) #Devuelve la tupla con el valor maximo en factor de la clave

## item 4
ordenarDiccionarioPorKey = lambda diccionario: dict(sorted(diccionario.items(), key=lambda item: limpiarTitulo(item[0]))) #Ordena un diccionario en funcion de las claves

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

## item 3,4
def imprimirTitulos(tituloColumnas,ancho):
    cantTitulos = len(tituloColumnas)
    print("-".center(ancho,"-"))
    for titulo in tituloColumnas:
        print(titulo.center(ancho//cantTitulos),end="")
    print()
    print("-".center(ancho,"-"))


## item 3
def espectadoresxSala(arch):
    espectadores = {}
    for linea in arch:
        linea = linea.strip()
        pelicula, año, sala = linea.split(";")
        if año not in espectadores:
            espectadores[año] = {}
        espectadores[año][sala] = espectadores[año].get(sala,0) + 1
    return espectadores

def imprimirTabla3ColumnasDict(arbol,ancho, tituloColumnas):
    """imprime un arbol base {key:{key:value},...} para hacerlo necesita el ancho que ocupara y los titulos para los dos encabezados"""
    imprimirTitulos(tituloColumnas,ancho)
    for key,value in arbol.items():
        ponerKey=True
        for key2,value2 in value.items():
            if ponerKey:
                print(key.center(ancho//3), end="")
                ponerKey = False
            else:
                print(" ".center(ancho//3), end="")
            print(key2.center(ancho//3), end="")
            print(str(value2).center(ancho//3))
            print()
        print("-".center(ancho,"-"))  
                  
## item 4
def quitarCaracteresEspeciales(palabra):
    """Separa la palabra de los signos de puntuacion anteriores y posteriores"""
    i = 0
    while i<len(palabra) and not palabra[i].isalnum():
        i += 1
    j = len(palabra)-1
    while j>i and not palabra[j].isalnum():
        j -= 1
    palabra = palabra [i:j+1]
    return palabra

def quitarAcentos(palabra):
    """quita los acentos de una palabra"""
    conTilde = "áéíóúÁÉÍÓÚ"
    sinTilde = "aeiouAEIOU"
    palabraSinAcentos = ""
    for i in palabra:
        if i in conTilde:
            posicion = conTilde.index(i)
            palabraSinAcentos += sinTilde[posicion]
        else:
            palabraSinAcentos += i
    return palabraSinAcentos

def limpiarTitulo(titulo):
    titulo = quitarCaracteresEspeciales(titulo)
    titulo = quitarAcentos(titulo)
    titulo = titulo.lower()
    return titulo

def imprimirTabla2ColumnasDict(diccionario, ancho, tituloColumnas):
    """imprime un diccionario base (key, value) para hacerlo necesita el ancho que ocupara y los titulos para los dos encabezados"""
    imprimirTitulos(tituloColumnas,ancho)
    for key,value in diccionario.items():
        print(key.center(ancho//2), end="")
        print(str(value).center(ancho//2))
        print("-".center(ancho,"-"))
#=========================================================================================================