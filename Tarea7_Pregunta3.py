supermercado = {}

print("Ingrese productos y sus cantidades (deje el nombre vacío para finalizar):")

while True:
    nombre_producto = input("Nombre del producto: ")
    if nombre_producto == "":
        break
    cantidad = int(input(f"Cantidad de {nombre_producto}: "))
    supermercado[nombre_producto] = cantidad

x = int(input("Ingrese el valor por el cual multiplicar las cantidades: "))

print("Productos y cantidades multiplicadas:")
for producto, cantidad in supermercado.items():
    print(f"{producto}: {cantidad * x}")
