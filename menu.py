from funciones_stark import *

def validar_entero(numero):
    """La función "validar_entero" comprueba si una entrada determinada es un número entero válido.

    Args:
        numero (_type_): El parámetro "numero" es una variable que representa un valor que queremos comprobar

    Returns:
        _type_: La función devuelve un valor booleano. Devuelve "Verdadero" si la entrada "numero" se puede convertir a un número entero y "Falso" en caso contrario.
    """

    try:
        int(numero)
        return True
    except ValueError:
        return False



def menu()->str:
    """
    Muestra un menú de opciones y solicita al usuario que ingrese una opción.

    Returns:
        str: La opción seleccionada por el usuario. 
    """
    limpiar_pantalla()
    print(f"{'menu de opciones':^50s}")
    print("1- Lista de super heroes")
    print("2- Altura de los super heroes")
    print("3- Super heroe mas alto")
    print("4. Super heroe mas bajo")
    print("5- Altura promedio de los super heroes")
    print("6- Nombre de super heroe mas alto y super heroe mas bajo")
    print("7- Super heroe mas pesado")
    print("8- Super heroe menos pesado")
    print("9- Salir")
    
    opcion = input("Por favor, ingrese el número de la opción elegida: ")

    if validar_entero(opcion):
        return int(opcion)
    else:
        return False
    
def pausar():
    """
    Pausa la ejecución del programa hasta que el usuario presione una tecla.
    """
    import os
    os.system("pause")
    
def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    import os
    os.system("cls")
    
def stark_marvel_app(lista_personaje)-> None:
    stark_normalizar_datos(lista_personaje)
    while True:
        
        match menu():
            case 1:
                stark_imprimir_nombres_heroes(lista_personajes)
            case 2:
                mostrar_altura_personajes(lista_personajes)
            case 3:
                mostar_super_mas_alto(lista_personajes)
            case 4:
                mostar_super_mas_bajo(lista_personajes)
            case 5:
                altura_promedio(lista_personajes)
            case 6:
                informar_superheroes_altura_max_min(lista_personajes)
            case 7:
                mostar_super_mas_pesado(lista_personajes)
            case 8:
                mostar_super_mas_liviano(lista_personajes)
            case 9:
                break
            case _:
                print("Opcion no valida")
            
        pausar()
     
     
def menu_2() -> str:
    """
    Muestra un menú de opciones y solicita al usuario que ingrese una opción.

    Returns:
        str: La opción seleccionada por el usuario. 
    """
    limpiar_pantalla()
    print(f"{'Menú de Opciones':^50s}")
    print("A- Superhéroes de género M")
    print("B- Superhéroes de género F")
    print("C- Superhéroe más alto de género M")
    print("D- Superhéroe más bajo de género M")
    print("E- Superhéroe más alto de género F")
    print("F- Superhéroe más bajo de género F")
    print("G- Altura promedio de los superhéroes de género M")
    print("H- Altura promedio de los superhéroes de género F")
    print("I- Nombre de superhéroes de los puntos C a F")
    print("J- Superhéroes con cada tipo de color de ojos")
    print("K- Superhéroes con cada tipo de color de pelo")
    print("L- Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("M- Todos los superhéroes agrupados por color de ojos")
    print("N- Todos los superhéroes agrupados por color de pelo")
    print("O- Todos los superhéroes agrupados por tipo de inteligencia")
    print("S- Salir")
    
    opcion = input("Por favor, ingrese la letra de la opción elegida: ").upper()
    return opcion


    
    
    
def stark_marvel_app_2(lista_personaje)-> None:
    stark_normalizar_datos(lista_personaje)
    while True:
        
        match menu_2():
            case "A":
                superheroes_por_genero(lista_personajes, "M")
            case "B":
                superheroes_por_genero(lista_personajes, "F")
            case "C":
                superheroe_mas_alto_M = super_mas_alto_genero(lista_personajes, "M")
                imprimir_superheroe_mas_alto_genero(superheroe_mas_alto_M, "masculino")
            case "D":
                super_heroe_mas_alto_f = super_mas_alto_genero(lista_personajes, "F")
                imprimir_superheroe_mas_alto_genero(super_heroe_mas_alto_f, "femenino")
            case "E":
                super_heroe_mas_bajo_m = super_mas_bajo_genero(lista_personajes, "M")
                imprimir_superheroe_mas_bajo_genero(super_heroe_mas_bajo_m)
            case "F":
                super_heroe_mas_bajo_f = super_mas_bajo_genero(lista_personajes, "F")
                imprimir_superheroe_mas_bajo_genero(super_heroe_mas_bajo_f)
            case "G":
                mostar_super_mas_pesado(lista_personajes)
            case "H":
                mostar_super_mas_liviano(lista_personajes)
            case "I":
                break
            case "J":
                break
            case "K":
                break
            case "L":
                break
            case "M":
                break
            case "N":
                break
            case "O":
                break
            case "S":
                break
            case _:
                print("Opcion no valida")
            
        pausar()