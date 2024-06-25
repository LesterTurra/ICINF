palabras = []

print("Ingrese palabras (deje en blanco para finalizar):")

while True:
    palabra = input()
    if palabra == "":
        break
    palabras.append(palabra)

for palabra in palabras:
    cuenta_a = palabra.lower().count('a')
    print(f"La palabra '{palabra}' tiene {cuenta_a} letras 'A' o 'a'.")
