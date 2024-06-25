lista = []

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "":
        break
    lista.append(palabra)

for x in lista:
    cont = 0
    for y in x:
        if y in("A","a"):
            cont = cont + 1
    print("La palabra ", x , " tiene ", cont , " letra A o a ")
