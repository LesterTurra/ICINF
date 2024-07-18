def digitos(num):
    num_str=str(num)
    cantidad_digitos=len(num_str)
    return cantidad_digitos

numero=input("Ingresa un numero:")

try:
    numero=int(numero)
    print("El numero", numero, "tiene", digitos(numero), "digitos.")
except ValueError:
    print("Por favor, ingresa un numero valido.")