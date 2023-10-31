def espectadoresAño(arch):
    """Crea un diccionario con la cantidad de entradas vendidas por año"""
    entradasAño = {}
    for entrada in arch:
        entrada = entrada.strip()
        pelicula, año, sala = entrada.split(";")
        entradasAño[año] = entradasAño.get(año, 0) + 1
    return entradasAño

def mejorAño(arch):
    """ejecuta el juego de acciones para oobtener el año con mayor cantidad de entradas vendidas"""
    espectadoresAño(arch)

#==================================================================================================
try:
    baseDeDatos = open("peliculas.txt","rt")
    print(espectadoresAño(baseDeDatos))
except OSError:
    print("error al abrir aechivo")
finally:
    try:
        baseDeDatos.close()
    except:
        pass