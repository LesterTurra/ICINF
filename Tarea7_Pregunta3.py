supermercado = {}

while True:
    producto = input("Nombre del producto: ")
    if producto == "":
        break
    cantidad = int(input("Ingrese la cantidad del producto : "))
    supermercado[producto] = cantidad

multiplicador = int(input("Ingrese el valor por el cual multiplicar las cantidades: "))

for x in supermercado:
    print("producto: ", x ," cantidad: ", supermercado[x] * multiplicador)
