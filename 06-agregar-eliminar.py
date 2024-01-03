mascotas = ["clarita", "pelusa", "chabela", "luna", "messi", "messi", "pulga"]
mascotas.insert(1, "ronaldo")  # AGREGAR UN VALOR EN CUALQUIER LADO DE LA LISTA
mascotas.append("mbappe")  # PARA AGREGAR UN ELEMENTO AL FINAL DE LA LISTA

# este solo elimina el primer dato duplicado por ejemplo si es el que queremos borrar
mascotas.remove("messi")

mascotas.pop(
    2
)  # para eliminar el ultimo elemento si no le pones nada en el () , pero tambien si quieres borrar lo que quieras pones el numero del elemento dentro del ()

del mascotas[0]  # para eliminar tambien

mascotas.clear()  # para eliminar todo

print(mascotas)
