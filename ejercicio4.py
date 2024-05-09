n=int(input("Ingrese un numero positivo de uno,dos,tres o cuatro digitos:"))

if n >= 1 and n <= 9:
    print("El numero tiene un digito.")
if n >= 10 and n <= 99:
    print("El numero tiene dos digitos.")
if n >= 100 and n <= 999:
    print("El numero tiene tres digitos.")
if n >= 1000 and n <= 9999:
    print("El numero tiene cuatro digitos.")