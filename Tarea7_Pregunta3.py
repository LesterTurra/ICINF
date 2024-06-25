supermercado = {}

print("Ingrese productos y sus cantidades (deje el nombre vacío para finalizar):")

# Bucle para ingresar productos y cantidades hasta que se ingrese un nombre vacío
while True:
    nombre_producto = input("Nombre del producto: ")
    if nombre_producto == "":
        break
    cantidad = int(input(f"Cantidad de {nombre_producto}: "))
    supermercado[nombre_producto] = cantidad

# Solicitar al usuario un valor X para multiplicar las cantidades
x = int(input("Ingrese el valor por el cual multiplicar las cantidades: "))

# Mostrar los productos y sus cantidades multiplicadas por X
print("Productos y cantidades multiplicadas:")
for producto, cantidad in supermercado.items():
    print(f"{producto}: {cantidad * x}")
