string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [
        char for char in texto if char != " "
    ]  # Esta función toma un string texto y devuelve una lista de caracteres que no son espacios


def cuenta_caracteres(
    lista,
):  # Esta función toma una lista de caracteres y devuelve un diccionario donde las claves son los caracteres y los valores son la cantidad de veces que aparecen
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(
    dict,
):  # Esta función toma un diccionario y lo ordena en función de los valores en orden descendente.
    return sorted(dict.items(), key=lambda key: key[1], reverse=True)


def mayores_tuplas(
    lista,
):  # Esta función toma una lista de tuplas ordenadas y devuelve un diccionario con los caracteres que tienen el máximo valor de repeticiones
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(
    diccionario,
):  # Esta función toma un diccionario y crea un mensaje formateado con los caracteres que más se repiten.
    mensaje = "los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(string)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(sin_espacios)
print(ordenados)
print(mayores)
print(mensaje)
# la de mayores tuplas quedo mal porque deberia dar e y s que son las que mas se repiten pero da los espacios como mayores veces se repiten
