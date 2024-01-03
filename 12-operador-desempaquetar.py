lista1 = [1, 2, 3, 4]
# print(1, 2, 3, 4,)
# print(*lista)

lista2 = [5, 6]

combinada = ["HOLA", *lista1, "mundo", *lista2]  # PARA COMBINAR LAS LISTAS
print(combinada)


# NO SE VA A HACER EL PRINT DE HOLA YA QUE SE REEMPLAZA EL VALOR porque se asignan las propiedades son de derecha a izq. si tengo una una propiedad x a la derecha y a la izquierda igual la izquierda la reemplaza la de la derecha y SI NO HAY VALOR EN EL IZQ LA DE LA DERECHA SE ASIGNA A LA DE LA IZQ.
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "holapepe", **punto2, "Z": "mundo"}
print(nuevoPunto)
