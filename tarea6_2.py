def mostrar_menu():
    print("Menú de opciones:")

def ingresar_elemento(lista):
    lista.append(input("Ingrese el elemento a agregar a la lista: "))
    print("Elemento agregado con éxito.")

def modificar_eliminar_elemento(lista, es_modificar):
    if not lista:
        print("La lista está vacía.")
        return
    indice = int(input("Ingrese el índice del elemento a modificar/eliminar: "))
    if indice < 0 or indice >= len(lista):
        print("Índice fuera de rango.")
        return
    if es_modificar:
        lista[indice] = input("Ingrese el nuevo valor para el elemento: ")
        print("Elemento modificado con éxito.")
    else:
        elemento_eliminado = lista[indice]
        del lista[indice]
        print("Elemento eliminado con éxito: " + elemento_eliminado)

def buscar_elemento(lista):
    if not lista:
        print("La lista está vacía.")
        return
    elemento = input("Ingrese el elemento a buscar: ")
    if elemento in lista:
        print("El elemento se encuentra en la lista: " + elemento)
    else:
        print("El elemento no se encuentra en la lista: " + elemento)

def mostrar_elementos(lista):
    if not lista:
        print("La lista está vacía.")
        return
    print("Elementos de la lista:")
    for indice in range(len(lista)):
        print(str(indice) + ": " + lista[indice])

def menu():
    mostrar_menu()
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    return opcion

lista = []
while True:
    opcion = menu()

    if opcion == '1':
        ingresar_elemento(lista)
    elif opcion == '2':
        modificar_eliminar_elemento(lista, es_modificar=True)
    elif opcion == '3':
        modificar_eliminar_elemento(lista, es_modificar=False)
    elif opcion == '4':
        if lista:
            print("Se eliminó el último elemento de la lista: " + lista[-1])
            del lista[-1]
        else:
            print("La lista está vacía.")
    elif opcion == '5':
        buscar_elemento(lista)
    elif opcion == '6':
        mostrar_elementos(lista)
    elif opcion == '7':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.")




