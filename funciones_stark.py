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
        print("-------------------------")
        print("Lista de superheroes")
        print("-------------------------")
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
        print("Nombre                     Altura")
        print("----------------------------------------")
        for superheroe in lista_personajes:
            print(f"{superheroe['nombre']: >20} | {superheroe['altura']:5.2f}")
    else:
        print("La lista de personajes está vacía.")

            
def mostar_super_mas_alto(lista_personajes: list) -> list:
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
    
def superheroes_por_genero(lista_personajes: list, genero):
    """_summary_

    Args:
        lista_personajes (list): _description_
        genero (_type_): _description_
    """
    print("----------------------------------")
    print(f"   Personajes de genero: {genero}.")
    print("----------------------------------")
    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            print(personaje['nombre'])
            

def super_mas_alto_genero(lista_personajes: list, genero: str) -> dict:
    """Encuentra al superhéroe más alto del género especificado en la lista.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
        genero (str): El género que se desea filtrar ("M" para masculino, "F" para femenino, etc.).

    Returns:
        dict: Un diccionario que contiene el nombre y la altura del superhéroe más alto del género especificado.
    """
    mas_alto = None
    
    for heroe in lista_personajes:
        if "genero" in heroe and heroe["genero"] == genero:
            if mas_alto is None or heroe["altura"] > mas_alto["altura"]:
                mas_alto = heroe
                
    return mas_alto

def imprimir_superheroe_mas_alto_genero(superheroe: dict, genero: str) -> None:
    """Imprime la información del superhéroe más alto del género especificado.

    Args:
        superheroe (dict): Un diccionario que representa al superhéroe más alto.
        genero (str): El género del superhéroe.

    Returns:
        None
    """
    if superheroe:
        print(f"El superhéroe más alto de género {genero} es: {superheroe['nombre']}, con una altura de {superheroe['altura']:.2f}")
    else:
        print(f"No se encontró ningún superhéroe de género {genero} en la lista.")
        
def super_mas_bajo_genero(lista_personajes: list, genero: str) -> dict:
    """Encuentra al superhéroe más alto del género especificado en la lista.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los personajes.
        genero (str): El género que se desea filtrar ("M" para masculino, "F" para femenino, etc.).

    Returns:
        dict: Un diccionario que contiene el nombre y la altura del superhéroe más alto del género especificado.
    """
    mas_bajo = None
    
    for heroe in lista_personajes:
        if "genero" in heroe and heroe["genero"] == genero:
            if mas_bajo is None or heroe["altura"] < mas_bajo["altura"]:
                mas_bajo = heroe
                
    return mas_bajo

def imprimir_superheroe_mas_bajo_genero(superheroe: dict, genero: str) -> None:
    """Imprime la información del superhéroe más alto del género especificado.

    Args:
        superheroe (dict): Un diccionario que representa al superhéroe más alto.
        genero (str): El género del superhéroe.

    Returns:
        None
    """
    if superheroe:
        print(f"El superhéroe más alto de género {genero} es: {superheroe['nombre']}, con una altura de {superheroe['altura']:.2f}")
    else:
        print(f"No se encontró ningún superhéroe de género {genero} en la lista.")

def altura_promedio_genero(lista_personajes: list, genero: str) -> float:
    """Calcula la altura promedio de los superhéroes del género especificado en la lista.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los superhéroes.
        genero (str): El género de los superhéroes para calcular la altura promedio ("M" para masculino, "F" para femenino, etc.).

    Returns:
        float: La altura promedio de los superhéroes del género especificado.
    """
    total_altura = 0
    total_superheroes = 0
    
    for heroe in lista_personajes:
        if "genero" in heroe and heroe["genero"] == genero:
            total_altura += heroe["altura"]
            total_superheroes += 1
            
    if total_superheroes == 0:
        return []
    else:
        return total_altura / total_superheroes


def imprimir_nombre_superheroe(superheroe: dict, genero: str, tipo: str) -> None:
    """Imprime el nombre del superhéroe asociado al resultado de una función.

    Args:
        superheroe (dict): Un diccionario que representa al superhéroe.
        genero (str): El género del superhéroe.
        tipo (str): El tipo de resultado ("alto" o "bajo").

    Returns:
        None
    """
    if superheroe:
        print(f"El superhéroe más {tipo} de género {genero} es: {superheroe['nombre']}")
    else:
        print(f"No se encontró ningún superhéroe {tipo} de género {genero} en la lista.")
        

def contar_superheroes_por_atributo(lista_personajes: list, atributo: str) -> dict:
    """
    Cuenta cuántos superhéroes hay para cada valor de un atributo dado.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los superhéroes.
        atributo (str): El atributo por el cual contar los superhéroes (e.g., 'color_ojos', 'color_pelo', 'inteligencia').

    Returns:
        dict: Un diccionario donde las claves son los valores del atributo y los valores son la cantidad de superhéroes con ese valor de atributo.
    """
    conteo_atributo = {}

    for personaje in lista_personajes:
        if atributo in personaje:
            valor_atributo = personaje[atributo] if personaje[atributo] else "No Tiene"
            if valor_atributo in conteo_atributo:
                conteo_atributo[valor_atributo] += 1
            else:
                conteo_atributo[valor_atributo] = 1

    return conteo_atributo


def imprimir_conteo_superheroes_por_atributo(conteo_superheroes: dict, atributo: str)-> str:
    """
    Imprime el conteo de superhéroes agrupados por un atributo específico.

    Args:
        conteo_superheroes (dict): Un diccionario donde las claves son los valores del atributo y los valores son la cantidad de superhéroes con ese atributo.
        atributo (str): El nombre del atributo por el cual se agruparon los superhéroes (por ejemplo, 'color de ojos', 'color de pelo', 'inteligencia').
    """
    print(f"Conteo de superhéroes por {atributo}:")
    print("------------------------------------------------")
    for clave, valor in conteo_superheroes.items():
        print(f"- {clave if clave else 'No Tiene'}: {valor}")



def agrupar_superheroes_por_atributo(lista_personajes: list, atributo: str) -> dict:
    """
    Agrupa los superhéroes por un atributo dado y devuelve un diccionario con los nombres de los superhéroes.

    Args:
        lista_personajes (list): Una lista de diccionarios que representan a los superhéroes.
        atributo (str): El atributo por el cual agrupar los superhéroes (e.g., 'color_ojos', 'color_pelo', 'inteligencia').

    Returns:
        dict: Un diccionario donde las claves son los valores del atributo y los valores son listas de nombres de superhéroes.
    """
    dic_superheroes_por_atributo = {}

    for personaje in lista_personajes:
        if atributo in personaje:
            valor_atributo = personaje[atributo]
            nombre_superheroe = personaje["nombre"]
            
            if valor_atributo in dic_superheroes_por_atributo:
                dic_superheroes_por_atributo[valor_atributo].append(nombre_superheroe)
            else:
                dic_superheroes_por_atributo[valor_atributo] = [nombre_superheroe]

    return dic_superheroes_por_atributo

def imprimir_superheroes_por_atributo(dic_superheroes: dict, atributo: str)-> str:
    """
    Imprime los superhéroes agrupados por un atributo específico.

    Args:
        dic_superheroes (dict): Un diccionario donde las claves son los valores del atributo y los valores son listas de nombres de superhéroes.
        atributo (str): El nombre del atributo por el cual se agruparon los superhéroes.
    """
    print(f"Superhéroes agrupados por {atributo}:")
    print("------------------------------------------------")
    for clave, lista_nombres in dic_superheroes.items():
        print(f"- {clave if clave else 'No Tiene'}: {', '.join(lista_nombres)}")









