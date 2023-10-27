from data_stark import lista_personajes
from os import system

def menu():
    from os import system
    system("cls")


    print("         **** Menu ****       ")
    print("1.Nombre de cada superheroe masculino")
    print("2.Nombre de cada superheroe femenino")
    print("3.El superhéroe más alto masculino")
    print("4.El superhéroe más alto femenino")
    print("5.el superhéroe más bajo masculino")
    print("6.el superhéroe más bajo femenino")
    print("7.Altura promedio de los masculinos")
    print("8.Altura promedio de los femeninos")
    print("9.Determinar cuántos superhéroes tienen cada tipo de color de ojos")
    print("10.Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("11.Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("12.Listar todos los superhéroes agrupados por color de ojos.")
    print("13.Listar todos los superhéroes agrupados por color de pelo.")
    print("14.Listar todos los superhéroes agrupados por inteligencia.")
    print("15.salir")

    opcion = input("Ingrese opcion: ")
    return opcion

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M

def nombre_m():
    for nombres_masculinos in lista_personajes:
        nombres = nombres_masculinos['nombre']
        genero = nombres_masculinos['genero']

        if genero == "M":
            print(f"El nombres de el superheroe es {nombres}")


# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F

def nombre_f():
    for nombres_femeninos in lista_personajes:
        nombres = nombres_femeninos['nombre']
        genero = nombres_femeninos['genero']

        if genero == "F":
            print(f"El nombres de la superheronia es {nombres}")


# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

def alto_m():
    mas_alto = 0
    nombre_Del_mas_alto = None
    for mas_alto_m in lista_personajes:
        nombre = mas_alto_m['nombre']
        alturas = float(mas_alto_m['altura'])
        genero = mas_alto_m['genero']

        if genero == "M" and alturas > mas_alto:
            mas_alto = alturas
            nombre_Del_mas_alto = nombre

    print(f"El nombres de el superheroe mas alto es {nombre_Del_mas_alto} con {mas_alto} cm")


# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F


def alto_f():
    mas_alta = 0
    nombre_Dela_mas_alta = None
    for mas_alto_f in lista_personajes:
        nombre = mas_alto_f['nombre']
        alturas = float(mas_alto_f['altura'])
        genero = mas_alto_f['genero']

        if genero == "F" and alturas > mas_alta:
            mas_alta = alturas
            nombre_Dela_mas_alta = nombre

    print(f"El nombres de el superheroe mas alto es {nombre_Dela_mas_alta} con {mas_alta} cm")


# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M


def bajo_m():
    mas_bajo = 99999
    nombre_Del_mas_bajo = None
    for mas_bajo_m in lista_personajes:
        nombre = mas_bajo_m['nombre']
        alturas = float(mas_bajo_m['altura'])
        genero = mas_bajo_m['genero']

        if genero == "M" and alturas < mas_bajo:
            mas_bajo = alturas
            nombre_Del_mas_bajo = nombre

    print(f"El nombres de el superheroe mas bajo es {nombre_Del_mas_bajo} con {mas_bajo} cm")


# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F

def baja_f():
    mas_baja = 99999
    nombre_Dela_mas_baja = None
    for mas_baja_f in lista_personajes:
        nombre = mas_baja_f['nombre']
        alturas = float(mas_baja_f['altura'])
        genero = mas_baja_f['genero']

        if genero == "F" and alturas < mas_baja:
            mas_baja = alturas
            nombre_Dela_mas_baja = nombre

    print(f"El nombres de el superheroe mas alto es {nombre_Dela_mas_baja} con {mas_baja} cm")


# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
def calculo_altura_promedio_m():
    acumulador = 0
    contador_altura_m = 0

    for altura_promedio_m in lista_personajes:
        alturas = float(altura_promedio_m['altura'])
        genero = altura_promedio_m['genero']

        if genero == "M" :
            acumulador += alturas
            contador_altura_m += 1 
            
            promedio_m = acumulador // contador_altura_m
            

    print(f"La altura promedio de las mujeres es {promedio_m} cm")


# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
def calculo_altura_promedio_f():
    acumulador = 0
    contador_altura_f = 0

    for altura_promedio_f in lista_personajes:
        alturas = float(altura_promedio_f['altura'])
        genero = altura_promedio_f['genero']

        if genero == "F" :
            acumulador += alturas
            contador_altura_f += 1 
            
            promedio = acumulador // contador_altura_f
            

    print(f"La altura promedio de las mujeres es {promedio} cm")


# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)

    # Deberia reutilizar las funciones?? no pude sacarlo si es asi. 


# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def color_de_ojos():
    contador_color_de_ojos = {}
    lista_color_de_ojos = []

    for ojos in lista_personajes:
        color_ojos = ojos['color_ojos'].lower()
        lista_color_de_ojos.append(color_ojos)

    for el_color in lista_color_de_ojos:
        if el_color in contador_color_de_ojos:
            contador_color_de_ojos[el_color] += 1
        else:
            contador_color_de_ojos[el_color] = 1

# recorre las dos a la ves
    for el_color, total in contador_color_de_ojos.items():
        print(f"El color de ojos {el_color} hay una cantidad de {total}")


# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

def tipo_de_pelo():
    contador_tipo_de_pelo = {}
    lista_tipo_de_pelo = []

    for pelo in lista_personajes:
        color_pelo = pelo['color_pelo'].lower()
        lista_tipo_de_pelo.append(color_pelo)

    for el_color in lista_tipo_de_pelo:
        if el_color in contador_tipo_de_pelo:
            contador_tipo_de_pelo[el_color] += 1
        else:
            contador_tipo_de_pelo[el_color] = 1
# recorre las dos a la ves
    for el_color, total in contador_tipo_de_pelo.items():
        print(f"Color de pelo {el_color}: {total}")


# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).


def determina_tipo_inteligencia():
    contador_de_inteligenica = {}
    lista_de_inteligencia = []
    tiene_inteligencia = False

    for inteligentes in lista_personajes:
        inteligencia = inteligentes['inteligencia'].lower()
        lista_de_inteligencia.append(inteligencia)

    for la_inteligencia in lista_de_inteligencia:
        if la_inteligencia in contador_de_inteligenica:
            contador_de_inteligenica[la_inteligencia] += 1
        else:
            contador_de_inteligenica[la_inteligencia] = 1

    if tiene_inteligencia:
        contador_de_inteligenica[""] = 0

# recorre las dos a la ves
    for la_inteligencia, total in contador_de_inteligenica.items():
        if la_inteligencia == "":
            print("No Tiene: " + str(total))
        else:
            print(f"Tipos de inteligencias {la_inteligencia}: {total}")




# M. Listar todos los superhéroes agrupados por color de ojos.

def color_de_ojos_agrupados():
    superheroes_por_color_de_ojos = {}  

    for ojos in lista_personajes:
        nombre = ojos['nombre']
        color_ojos = ojos['color_ojos'].lower()

        if color_ojos in superheroes_por_color_de_ojos:
            superheroes_por_color_de_ojos[color_ojos].append(nombre)
        else:
            superheroes_por_color_de_ojos[color_ojos] = [nombre]

    for color, superheroes in superheroes_por_color_de_ojos.items():
        print(f"Superhéroes con color de ojos {color}:")
        for nombre in superheroes:
            print(nombre)



# N. Listar todos los superhéroes agrupados por color de pelo.

def color_de_pelo_agrupados():
    superheroes_por_color_de_pelo = {}  

    for pelito in lista_personajes:
        nombre = pelito['nombre']
        color_de_pelo = pelito['color_pelo']

        if color_de_pelo in superheroes_por_color_de_pelo:
            superheroes_por_color_de_pelo[color_de_pelo].append(nombre)
        else:
            superheroes_por_color_de_pelo[color_de_pelo] = [nombre]

    for color, superheroes in superheroes_por_color_de_pelo.items():
        print(f"Superhéroes con color de pelo {color}:")
        for nombre in superheroes:
            print(nombre)



# O. Listar todos los superhéroes agrupados por tipo de inteligencia
def agrupados_por_inteligencia():
    superheroes_por_inteligencia = {}  

    for los_inteligentes in lista_personajes:
        nombre = los_inteligentes['nombre']
        inteligencia = los_inteligentes['inteligencia'].upper()

        if inteligencia in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia].append(nombre)
        else:
            superheroes_por_inteligencia[inteligencia] = [nombre]

    for inteligentes, superheroes in superheroes_por_inteligencia.items():
        print(f"Superhéroes y su tipo de inteligencia {inteligentes}:")
        for nombre in superheroes:
            print(nombre)




while True:
    match (menu()):
        case "1":
            nombre_m()
        case "2":
            nombre_f()
        case "3":
            alto_m()
        case "4":
            alto_f()
        case "5":
            bajo_m()

        case "6":
            baja_f()

        case "7":
            calculo_altura_promedio_m()

        case "8":
            calculo_altura_promedio_f()
        case "9":
            color_de_ojos()
        case "10":
            tipo_de_pelo()
        case "11":
            determina_tipo_inteligencia()
        case "12":
            color_de_ojos_agrupados()
        case "13":
            color_de_pelo_agrupados()
        case "14":
            agrupados_por_inteligencia()
        case "15":
            break

    system("pause")