def contar_vocales_consonantes(palabra):
    vocales = 'aeiouAEIOU'
    num_vocales = sum(1 for letra in palabra if letra in vocales)
    num_consonantes = sum(1 for letra in palabra if letra not in vocales)
    return num_vocales, num_consonantes

palabras = []
palabra = input("Ingrese una palabra (deje vacío para finalizar): ")

while palabra:
    palabras.append(palabra)
    palabra = input("Ingrese otra palabra (deje vacío para finalizar): ")

print("Cantidad de vocales y consonantes de cada palabra:")
for palabra in palabras:
    vocales, consonantes = contar_vocales_consonantes(palabra)
    print("Palabra:", palabra)
    print("Vocales:", vocales)
    print("Consonantes:", consonantes)
    print()


