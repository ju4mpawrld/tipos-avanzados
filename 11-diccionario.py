# los diccionario son una coleccion de datos que se encuentran agrupados por una llave y un valor.
# A LA IZQUIERDA SOLO ACEPTA STRINGS(X) Y LO DE LA DERECHA LO QUE SEA(25)
punto = {"x": 25, "y": 50}
print(punto)
# PARA ACCEDER A UN VALOR SE HACE CON EL STRING:
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["cr7"])  # LLAVE IGUAL = STRING
if "cr7" in punto:
    print("encontre a cr7", punto["cr7"])

print(punto.get("x"))
print(punto.get("cr7", 7))  # PARA AGREGAR
del punto["x"]  # PARA ELIMINAR UNA LLAVE
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():  # TODAS LAS MANERAS DE ACCEDER A LOS DICCIONARIOS ANASHEIII
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [  # CUANDO ESTAMAOS TRABAJANDO CON ELEMENTOS QUE VIENEN DE UNA BASE DE DATOS VAMOS A TENER QUE TENER UN IDENTIFICADOR UNICO (COMO EL RUT) OSEA ALGO QUE SOLO TIENES ASOCIADO TU
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "feliz"},
    {"id": 3, "nombre": "juampa"},
    {"id": 4, "nombre": "vicente"},
]

for usuario in usuarios:
    print(usuario["nombre"])
