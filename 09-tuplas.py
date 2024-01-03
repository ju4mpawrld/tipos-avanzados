# una tupla es lo mismo que una lista pero la diferencia que hay es que la tupla no la puedes modificar(ni agregar elementos ni sacar etc....) y ademas
# tenemso que ocuapr los parentesis ()
numeros = (1, 2, 3, 4) + (5, 6, 7)
print(numeros)

# COMANDO TUPLE PARA CAMBIAR DE LISTAS A TUPLA OBVIAMENTE
punto = tuple([1, 2])
print(punto)  # todas operaciones podemos ocupar tuplas menos apent y pop
for n in numeros:  # also iterar las tuplas
    print(n)
listaNumeros = list(numeros)
# ESTO PARA SI QUEREMOS MIDIFICARLO (QUE NO LO DEBERIAMOS HACERLO) ,LO QUE HICIMOS FUE CRAR UNA LISTA EN BASE A LA TUPLA Y MODIFICAMOS LA LISTA PERO NO LA TUPLA
listaNumeros[0] = "CHANCHITO FELIZ"
print(listaNumeros)
