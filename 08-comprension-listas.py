Usuarios = [
    ["pepe", 4],
    ["gonzalo", 1],
    ["loñio", 5],
]  # esta lista tiene dos elementos: nombre y id.

# nombres = []
# for usuario in Usuarios:
#     nombres.append(usuario[0])          hay una forma mas eleganate de hacerlo que es la de abajo
# print(nombres)

# transformacion:     la vamos a conocer como MAP
nombres = [usuario[0] for usuario in Usuarios]

# filtrar:  la vamos a conocer como filter
nombres = [usuario for usuario in Usuarios if usuario[1] > 2]
print(nombres)

# filtrar y tranformar
nombres = [usuario[0] for usuario in Usuarios if usuario[1] > 2]
print(nombres)
