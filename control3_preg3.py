def potencia(num,exp):
    if exp==0:
        return 1
    else:
        return num*potencia(num,exp-1)
    
numero=int(input("Ingresa un numero:"))
exponente=int(input("Ingresa el exponente:"))

resultado=potencia(numero,exponente)
print("el resultado de",numero,"elevado a",exponente,"es",resultado)