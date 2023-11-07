# filtrarEntradasPorTitulo - maximoDiccionario - porcentaje (maximoDiccionario(dicc)[1])*100)/sum(dicc.values())
## filtrarEntradasPorAño - maximoDiccionario
### espectadoresxSala - ordenarDiccionarioPorKey - imprimirTabla3ColumnasDict
#### filtrarEntradasPorTitulo - ordenarDiccionarioPorKey - imprimirTabla2ColumnasDict
##### PeliculaSala - mejorCombo
###### salasTransmitidas - filtrarPeliculasMayorSala - imprimirLista

# Funciones
## Filtracion
def filtrarEntradasPorTitulo(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por titulo, 
    sin importar el periodo y sala"""
    dic={}
    for linea in arch:
        linea = linea.strip()
        nombre, año, sala=linea.split(";") #Desempaquetado de datos
        dic[nombre]=dic.get(nombre,0) + 1 #agrega y acumula
    return dic 

def filtrarEntradasPorAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año, 
    sin importar el titulo y sala"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño

def espectadoresxSala(arch):
    """Crea un arbol donde primero se establce los años y dentro la cantidad de 
    entradas vendidas por sala, sin importar titulo"""
    espectadores = {}
    for linea in arch:
        linea = linea.strip()
        pelicula, año, sala = linea.split(";")
        if año not in espectadores:
            espectadores[año] = {}
        espectadores[año][sala] = espectadores[año].get(sala,0) + 1
    return espectadores

def peliculaSala(arch):
    """Crea un arbol donde primero se establce los titulos y dentro la cantidad de 
    entradas vendidas por sala, sin importar año"""
    filtrado = {}
    for linea in arch:
        linea = linea.strip()
        pelicula, año, sala = linea.split(";")
        if pelicula not in filtrado:
            filtrado[pelicula] = {}
        filtrado[pelicula][sala] = filtrado[pelicula].get(sala,0) + 1
    return filtrado

def salasTransmitidas(archivo):
    """Crea un diccionario donde relacion titulos de peliculas con un conjunto de 
    las salas en la que fue transmitida"""
    salas = {}
    for linea in archivo:
        linea = linea.strip()
        pelicula, año, sala = linea.split(";")
        if pelicula not in salas:
            salas[pelicula] = set()
        salas[pelicula].add(sala)
    return salas

## Procesamiento
reglasTresSimples = lambda x,y,z: (x*y)/z 
    #Porcentaje, x=maximo, y=100, z= el total

maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda item: item[1]) 
    #Devuelve la tupla con el valor maximo en factor de la clave

ordenarDiccionarioPorKey = lambda diccionario: dict(sorted(diccionario.items(), key=lambda item: limpiarTitulo(item[0]))) 
    #Ordena un diccionario en funcion de las claves

mayorCantidadDeSalas = lambda diccionario: len(max(diccionario.values(), key=lambda x: len(x))) 
    # Devuelve la longitud del iterable de mayor longitud de un diccionario

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
    """Ejecuta serie de comandos para dejar titulo sin caracteres especiales dejando de A-Z,1-9"""
    titulo = quitarCaracteresEspeciales(titulo)
    titulo = quitarAcentos(titulo)
    titulo = titulo.lower()
    return titulo

def filtrarPeliculasMayorSalas(diccionario):
    """Crea una lista con aquellas peliculas que tienen la mayor cantidad de salas transmitidas"""
    mayor = mayorCantidadDeSalas(diccionario)
    filtrado = [key for key,value in diccionario.items() if len(value)==mayor]
    return filtrado

def mejorCombo(diccionario):
    """Calcula la mejor combinacion sala/pelicula sin importar el año, devuelve una tupla con el nombre de la pelicula y 
    una tupla con la informacion de la sala"""
    print(diccionario)
    diccionario = {key: maximoDiccionario(value) for key,value in diccionario.items()}
    print(sorted(diccionario.items(), key=lambda item: item[1][1], reverse=True))
    combo = max(diccionario.items(), key=lambda item: item[1][1])
    return combo

## Pantalla
def imprimirTitulos(tituloColumnas,ancho):
    """Imprime serie de titulos en un ancho especifico de manera equitativa"""
    cantTitulos = len(tituloColumnas)
    print("-".center(ancho,"-"))
    for titulo in tituloColumnas:
        print(titulo.center(ancho//cantTitulos),end="")
    print()
    print("-".center(ancho,"-"))

def imprimirLista(lista,ancho,titulo):
    """Imprime tabla de una columna"""
    imprimirTitulos([titulo],ancho)
    for i in lista:
        print(i.center(ancho))
        print("-".center(ancho,"-"))

def imprimirTabla2ColumnasDict(diccionario, ancho, tituloColumnas):
    """imprime un diccionario base (key, value) para hacerlo necesita el ancho que ocupara 
    y los titulos para los dos encabezados"""
    imprimirTitulos(tituloColumnas,ancho)
    for key,value in diccionario.items():
        print(key.center(ancho//2), end="")
        print(str(value).center(ancho//2))
        print("-".center(ancho,"-"))

def imprimirTabla3ColumnasDict(arbol,ancho, tituloColumnas):
    """imprime un arbol base {key:{key:value},...} para hacerlo necesita el ancho que ocupara 
    y los titulos para los dos encabezados"""
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
#=========================================================================================================