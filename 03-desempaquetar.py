# numeros = [1, 2, 3]

# feo
# primero = numeros [0]
# segundo = numeros [1]
# tercero = numeros [2]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, tercero = numeros
print(numeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
