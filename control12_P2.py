nombres = []

for i in range(7):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombres_sin_a = [nombre for nombre in nombres if not nombre.endswith("a")]

print("Lista sin nombres que terminen con 'a':")
for nombre in nombres_sin_a:
    print(nombre)