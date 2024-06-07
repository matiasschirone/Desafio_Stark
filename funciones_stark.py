from data_stark import lista_personajes

def stark_normalizar_datos(lista_personajes: list) -> None:
    """
    La función recorre la lista de héroes y convierte las alturas, pesos
    y fuerzas de cadena a tipo numérico (float) si es necesario.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los héroes.

    Returns:
        None
    """
    if len(lista_personajes) == 0:
        print("Error: La lista de héroes está vacía")
        return

    datos_modificados = False

    for heroe in lista_personajes:
        if "altura" in heroe and isinstance(heroe["altura"], str):
            heroe["altura"] = float(heroe["altura"])
            datos_modificados = True
        if "peso" in heroe and isinstance(heroe["peso"], str):
            heroe["peso"] = float(heroe["peso"])
            datos_modificados = True
        if "fuerza" in heroe and isinstance(heroe["fuerza"], str):
            heroe["fuerza"] = float(heroe["fuerza"])
            datos_modificados = True

    if datos_modificados:
        print("Datos normalizados")

def obtener_nombre(dic_heroe: dict) -> str:
    """Obtiene el nombre de un héroe.

    Args:
        dic_heroe (dict): Un diccionario que representa a un héroe.

    Returns:
        str: El nombre del héroe.
    """
    return f"Nombre: {dic_heroe['nombre']}"


def stark_imprimir_nombres_heroes(lista_personajes: list) -> None:
    """Imprime los nombres de los héroes.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los héroes.

    Raises:
        ValueError: Si la lista de personajes está vacía.
    """
    try:
        if not lista_personajes:
            raise ValueError("La lista de personajes no puede estar vacía")
        
        for heroe in lista_personajes:
            nombre = obtener_nombre(heroe)
            print(nombre)
    except ValueError as e:
        print(e)
        
def mostrar_altura_personajes(lista_personajes: list) -> None:
    """Muestra los nombres y alturas de los personajes.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    if lista_personajes:
        print("Nombre         Altura")
        print("------------------------")
        for superheroe in lista_personajes:
            print(f"{superheroe['nombre']: <10} | {superheroe['altura']:5.2f}")
    else:
        print("La lista de personajes está vacía.")

            
def mostar_super_mas_alto(lista_personajes: list) -> None:
    """Muestra al superhéroe más alto.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    maximo_altura = 0 
    
    for superheroe in range(len(lista_personajes)):
        if superheroe == 0 or lista_personajes[maximo_altura]["altura"] < lista_personajes[superheroe]["altura"]:
            maximo_altura = superheroe

    nombre = lista_personajes[maximo_altura]["nombre"]
    altura = lista_personajes[maximo_altura]["altura"]
    print(f"El superhéroe más alto es: {nombre} y tiene {altura} de altura")

def mostar_super_mas_bajo(lista_personajes: list) -> None:
    """Muestra al superhéroe más bajo.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    minimo_altura = 0  

    for superheroe in range(len(lista_personajes)):
        if superheroe == 0 or lista_personajes[minimo_altura]["altura"] > lista_personajes[superheroe]["altura"]:
            minimo_altura = superheroe

    nombre = lista_personajes[minimo_altura]["nombre"]
    altura = lista_personajes[minimo_altura]["altura"]
    print(f"El superhéroe más bajo es: {nombre} y tiene {altura} de altura")
    
def informar_superheroes_altura_max_min(lista_personajes: list)-> str:
    """Informa el nombre del superhéroe asociado al indicador de altura MÁXIMO y MÍNIMO.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los superhéroes.

    Returns:
        str: Una cadena que contiene el nombre del superhéroe más alto y más bajo.
    """
    mas_alto = mostar_super_mas_alto(lista_personajes)
    mas_bajo = mostar_super_mas_bajo(lista_personajes)
    
    return (f"{mas_alto}\n {mas_bajo}")


def altura_promedio(lista_personajes: list) -> None:
    """Calcula y muestra la altura promedio de los personajes.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    acumulador_altura_heroes = 0
    for heroe in lista_personajes:
        acumulador_altura_heroes += heroe["altura"]

    promedio_altura = acumulador_altura_heroes / len(lista_personajes)
    print(f"La altura promedio es: {promedio_altura:.2f}")

def mostar_super_mas_pesado(lista_personajes: list) -> None:
    """Muestra al superhéroe más pesado.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    maximo_peso = 0 

    for superheroe in range(len(lista_personajes)):
        if superheroe == 0 or lista_personajes[maximo_peso]["peso"] < lista_personajes[superheroe]["peso"]:
            maximo_peso = superheroe

    nombre = lista_personajes[maximo_peso]["nombre"]
    peso = lista_personajes[maximo_peso]["peso"]
    print(f"El superhéroe más pesado es: {nombre} con {peso} kg.")

def mostar_super_mas_liviano(lista_personajes: list) -> None:
    """Muestra al superhéroe más liviano.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
    """
    minimo_peso = 0  

    for superheroe in range(len(lista_personajes)):
        if superheroe == 0 or lista_personajes[minimo_peso]["peso"] > lista_personajes[superheroe]["peso"]:
            minimo_peso = superheroe

    nombre = lista_personajes[minimo_peso]["nombre"]
    peso = lista_personajes[minimo_peso]["peso"]
    print(f"El superhéroe más liviano es: {nombre} con {peso} kg.")
