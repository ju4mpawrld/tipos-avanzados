mascotas = ["clarita", "pelusa", "chabela", "luna"]
print(mascotas[0])  # clarita = 0 , pelusa = 1 chabela = 2 , luna = 3
mascotas[0] = "bicho"  # PARA REEMPLAZAR
print(mascotas[0:3])
print(mascotas[:4])
print(mascotas[2:])  # por logica me toma el ultimo elemento (LUNA)
# # -1 vendria siendo uno a la izquierda pero no hay nada asi que se va hacia el final que es (LUNA)
print(mascotas[-1])
print(mascotas[::2])
print(mascotas[1::2])
print(mascotas[0::2])
numeros = list(range(1, 21))
print(numeros[::2])
print(numeros[1::2])
