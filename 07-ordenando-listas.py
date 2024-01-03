numeros = [34, 3, 88, 6, 545, 23]

numeros.sort()  # para poner los numeros en orden
print(numeros)
numeros.sort(reverse=True)
print(numeros)


# SORTED DEVUELVE UNA NUEVA LISTA Y NO AFECTA LA LISTA ANTERIOR(ESA ES LA DIFERENCIA ENTRE SORTED Y SORT)
numeros2 = sorted(numeros)  # reverse=True
print(numeros2)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# si el primer elemento es ordenable, en ese caso si la va a ordenar.
usuarios = [["pepe", 4], ["gonzalo", 1], ["loñio", 5]]
# pero si ponemos los numeros al final como ahora necesariamente hay que indicarle a sort como nosotros queremos que ordene los elementos de la lista y esto se hace por las funciones:


# def ordena(elemento):
#     return elemento[1]

# usuarios.sort(key=ordena)
# print(usuarios)
# pero esto se ve feo y lo de abajo es elegante.

usuarios.sort(key=lambda el: el[1])  # es para ordenar pero asi se escribe bien
print(usuarios)
