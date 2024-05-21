estatura = 1
suma = 0
c = 0
while estatura > 0:
    estatura = float(input("Ingresa una estatura: "))
    if estatura > 0:
        suma += estatura
        c += 1

if c > 0:
    print(f"El promedio de estaturas es: {suma/c}")