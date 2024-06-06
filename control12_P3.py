palabras = []

while True:
    palabra = input("Ingrese una palabra (presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras.append(palabra)

if palabras:  
    longitud_minima = min(len(palabra) for palabra in palabras)
    print("La palabra más corta tiene", longitud_minima, "caracteres.")
else:
    print("No se ingresaron palabras.")