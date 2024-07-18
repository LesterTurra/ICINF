def es_binario(var):
    for c in var:
        if c!='0'and c!='1':
            return False
        return True
    
cadena=input("Ingresa una cadena:")

if es_binario(cadena):
    print("La cadena", cadena, "es una expresión binaria.")
else:
    print("La cadena",cadena,"no es una expresión binaria.")

