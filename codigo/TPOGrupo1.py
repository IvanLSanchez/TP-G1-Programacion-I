# Funciones
## Filtracion
def filtrarEntradasPorTitulo(archivo,diccionario):
    """LLena un diccionario con la cantidad de entradas vendidas por titulo, 
    sin importar el período y sala."""
    for entrada in archivo:
        entrada = entrada.strip()
        pelicula,año,sala = entrada.split(";") #Desempaquetado de datos
        diccionario[pelicula] = diccionario.get(pelicula,0) + 1 #agrega y acumula

def filtrarEntradasPorAño(archivo,diccionario):
    """LLena un diccionario con la cantidad de entradas vendidas por año, 
    sin importar el título y sala."""
    for entrada in archivo:
        entrada = entrada.strip()
        pelicula,año,sala = entrada.split(";")
        diccionario[año] = diccionario.get(año, 0) + 1

def filtrarEntradasPorAñoYSala(archivo,diccionario):
    """LLena un árbol donde primero se establce los años y dentro la cantidad de 
    entradas vendidas por sala, sin importar título."""
    for entrada in archivo:
        entrada = entrada.strip()
        pelicula,año,sala = entrada.split(";")
        if año not in diccionario:
            diccionario[año] = {}
        diccionario[año][sala] = diccionario[año].get(sala,0) + 1

def filtrarEntradasPorPeliculaYSala(archivo,diccionario):
    """LLena un arbol donde primero se establce los títulos y dentro la cantidad de 
    entradas vendidas por sala, sin importar año."""
    for entrada in archivo:
        entrada = entrada.strip()
        pelicula,año,sala = entrada.split(";")
        if pelicula not in diccionario:
            diccionario[pelicula] = {}
        diccionario[pelicula][sala] = diccionario[pelicula].get(sala,0) + 1

## Procesamiento.
reglasTresSimples = lambda x,y,z: (x*y)/z 
    #Porcentaje.

maximoDiccionario = lambda diccionario: max(diccionario.items(), key=lambda item: item[1]) 
    #Devuelve la tupla con el valor maximo en factor de la clave.

ordenarDiccionarioPorKey = lambda diccionario: dict(sorted(diccionario.items(), key=lambda item: limpiarTitulo(item[0]))) 
    #Ordena un diccionario en funcion de las claves.

maximaLongitudValues = lambda diccionario: len(max(diccionario.values(), key=lambda item: len(item))) 
    # Devuelve la longitud del iterable de mayor longitud de un diccionario.

def quitarCaracteresEspeciales(palabra):
    """Separa la palabra de los signos de puntuación anteriores y posteriores."""
    i = 0
    while i<len(palabra) and not palabra[i].isalnum():
        i += 1
    j = len(palabra)-1
    while j>i and not palabra[j].isalnum():
        j -= 1
    palabraSinCaracteres = palabra [i:j+1]
    return palabraSinCaracteres

def quitarAcentos(palabra):
    """Quita los acentos de una palabra."""
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
    """Ejecuta serie de comandos para dejar título sin caracteres especiales dejando de A-Z,1-9."""
    titulo = quitarCaracteresEspeciales(titulo)
    titulo = quitarAcentos(titulo)
    titulo = titulo.lower()
    return titulo

def peliculasConMasSalas(diccionario):
    """Crea una lista con aquellas películas que tienen la mayor cantidad de salas transmitidas."""
    mayor = maximaLongitudValues(diccionario)
    filtrado = [key for key,value in diccionario.items() if len(value)==mayor]
    return filtrado

def mejorComboSalaPelicula(diccionario):
    """Calcula la mejor combinación sala/película sin importar el año, devuelve una tupla con el nombre de la película y 
    una tupla con la información de la sala."""
    for key,value in diccionario.items():
        diccionario[key] = maximoDiccionario(value)
    combo = max(diccionario.items(), key=lambda item: item[1][1])
    return combo

## Pantalla
def accion():
    while True:
        try:
            opcion = int(input("""
¿Qué acción desea realizar?
1) Pelicula más taquillera.
2) Año con mayor cantidad de espectadores.
3) Cantidad de espectadores por sala cada año.
4) Cantidad de espectadores de cada película.
5) Sala-película más convocante.
6) Película con mayor cantidad de salas.
7) Salir.
Respuesta (indique numero de opción): """))
            assert opcion>=1 and opcion<=7
            break
        except ValueError:
            print("\nSolo se aceptan numeros. Intente nuevamente.\n")
        except AssertionError:
            print("\nSolo se permiten numeross del 1 al 7. Intente nuevamente.\n")
    return opcion 

def imprimirTitulos(tituloColumnas,ancho):
    """Imprime serie de títulos en un ancho específico de manera equitativa."""
    print("-".center(ancho,"-"))
    anchoColumna = ancho//len(tituloColumnas)
    for titulo in tituloColumnas:
        print(titulo.center(anchoColumna),end="")
    print()
    print("-".center(ancho,"-"))

def imprimirLista(lista,ancho):
    """Imprime tabla de una columna."""
    if len(lista) == 1:
        print(lista[0].center(ancho))
        print("-".center(ancho,"-"))
    else:
        print(lista[0].center(ancho))
        print("-".center(ancho,"-"))
        imprimirLista(lista[1:],ancho)

def imprimirTabla2ColumnasDict(diccionario,ancho,tituloColumnas):
    """Imprime un diccionario base (key, value) para hacerlo necesita el ancho que ocupará
    y los títulos para los dos encabezados."""
    imprimirTitulos(tituloColumnas,ancho)
    anchoColumna = ancho // 2
    for key,value in diccionario.items():
        print(key.center(anchoColumna), end="")
        print(str(value).center(anchoColumna))
        print("-".center(ancho,"-"))

def imprimirTabla3ColumnasDict(arbol,ancho, tituloColumnas):
    """Imprime un árbol base {key:{key:value},...} para hacerlo necesita el ancho que ocupará 
    y los títulos para los dos encabezados."""
    imprimirTitulos(tituloColumnas,ancho)
    anchoColumna = ancho//3
    for key,value in arbol.items():
        ponerKey=True
        for key2,value2 in value.items():
            if ponerKey:
                print(key.center(anchoColumna), end="")
                ponerKey = False
            else:
                print(" ".center(anchoColumna), end="")
            print(key2.center(anchoColumna), end="")
            print(str(value2).center(anchoColumna))
            print()
        print("-".center(ancho,"-"))
#=========================================================================================================
try:
    baseDeDatos = open("codigo/basesDeDatos/peliculas.txt","rt")
    print("Bienvenidos al centro de estadísticas de cines mcPato.")
    opcion = accion()
    while opcion != 7:
        print()
        filtracion={}
        if opcion == 1:
            filtrarEntradasPorTitulo(baseDeDatos, filtracion)
            masTaquillera=maximoDiccionario(filtracion)
            porcentaje=reglasTresSimples(masTaquillera[1],100,sum(filtracion.values()))
            print(f"La película más taquillera fue '{masTaquillera[0]}' con una cantidad de {masTaquillera[1]} entradas vendidas. El porcentaje de ventas es de {porcentaje:.2f}%.")            
        elif opcion == 2:
            filtrarEntradasPorAño(baseDeDatos, filtracion)
            añoMasConvocante=maximoDiccionario(filtracion)
            print(f"El año más convocante fue: {añoMasConvocante[0]}.")
        elif opcion == 3:
            filtrarEntradasPorAñoYSala(baseDeDatos, filtracion)
            filtracion=ordenarDiccionarioPorKey(filtracion)
            imprimirTabla3ColumnasDict(filtracion,150,["Año", "Sala", "Cantidad de espectadores"])
        elif opcion == 4:
            filtrarEntradasPorTitulo(baseDeDatos, filtracion)
            filtracion=ordenarDiccionarioPorKey(filtracion)
            imprimirTabla2ColumnasDict(filtracion,100,["Película","Cantidad de espectadores"])
        elif opcion == 5:
            filtrarEntradasPorPeliculaYSala(baseDeDatos, filtracion)
            combo=mejorComboSalaPelicula(filtracion) 
            print(f"La mejor combinación sala - película es: '{combo[0]}' - sala {combo[1][0]}.")
        else:
            filtrarEntradasPorPeliculaYSala(baseDeDatos, filtracion)
            filtrarPeliculasMayor=peliculasConMasSalas(filtracion)
            imprimirTitulos(["Pelicula con mayor cantidad de salas"],100)
            imprimirLista(filtrarPeliculasMayor,100)
        while True:
            try:
                seguir = input("¿Desea realizar otra función? (Y/N): ")
                assert seguir.isalpha(), "\nSolo insertar letras. Intente nuevamente.\n"
                seguir = seguir.upper()
                assert seguir == "Y" or seguir == "N", "\nSolo insertar 'Y' (yes) o 'N' (not). Intente nuevamente.\n"
                opcion = accion() if seguir == "Y" else 7
                if seguir == "Y":
                    baseDeDatos.seek(0)
                break
            except AssertionError as mensaje:
                print(mensaje)
    print("\nGracias por visitar el centro de estadísticas de cines mcPato.")
except OSError:
    print("Error al abrir aechivo.")
finally:
    try:
        baseDeDatos.close()
    except:
        pass
    
"""
                                                    
          *%%@@@@@@                                 
        #%%%@@@@@@@%                                
       %@%%%@@@@@@@@%                               
      @@@%%@@@@@@@@@@#                              
     #@@@@%%@@@@@@@@@@                              
      %@@@%%@%@@#+++++#  %@%                        
        %@@@@%+++++++*%@@@@@                        
          %@#+@@@@@@@@@@-.%@                        
            @@@@@*......:.:#                        
           #@@@@#::. .-.:. :*=*                     
           @@@%..-.   .-:-*.-.=*                    
           @@@#..-..#. .-*%+:+::+                   
            *+--..=.@#..:-%*=+::#                   
           =..:=+..-=@+::-===-===*                  
          #*...++==:-:=+=+---+*+*                   
           *...-+***=----=+=**                      
             +=      #%%#@                          
                      *-.-#                         
           *%%%%%##**#@#.-@%#                       
         ###*********#@@*-@%***                     
         %#***#*##%*#*@@@@@@***##                   
         ***#%%*   =***%#**#*******%                
         #%@@@%+:.*#*********#**#****##             
        +-@@=...*::@#********% #********%@%         
      +::::*:.:.-***%@@@+==@@#   #***#@@@@*.....-+  
      -.-..**=.#.=*******#***##    #*@@@@*=.*@*.=:+ 
     *-=#+.%******#***#**-***##*     #@@@%=..-..-:+ 
         #.=**#****#*#***.****##        #*%@%===::% 
         *::***#****#**#:..****##        *@@   #@@% 
          +.****###****=...=****#        @@   #@@   
          #..+*********...:*#***%       @@#   ##    
           *+-+*******...=* #**#       #@%          
           *-*+#****#  *+    **%      #@%           
          *-=*   #*#   +=#            @@            
          =-%          #-+           @@             
         *===          +==*         *@              
         %==%           %@@        %@%              
        *@@@          #+@@@@@@%%%#%@#*              
     %@%@@@@%          @@@@@@@@@*-##----==+         
   %@@@@@@@@@%            %@@@*--##-----=+          
  %%#*++====++*#                *-*++#              
 *=-------------=#                                  
 +**+=--------=**#                                  
       *##+*#         
"""
