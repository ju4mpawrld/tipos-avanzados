lista = [65, 64, 213, 11, 45]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista2 = [1, 3, 2, 5, 4]
lista2 = sorted(lista)
print(lista2)

usuarios = [["pepe", 4], ["gonzalo", 1], ["loñio", 5]]
usuarios.sort(key=lambda us: us[1])
print(usuarios)
