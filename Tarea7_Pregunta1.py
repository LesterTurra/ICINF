
numeros = []

for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

print("Números en orden inverso:")
for numero in reversed(numeros):
    print(numero)