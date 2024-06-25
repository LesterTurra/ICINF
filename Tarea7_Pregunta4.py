deudores = {}

print("Ingrese el RUT y la deuda de 5 personas:")
for x in range(5):
    while True:
        try:
            rut = int(input("Ingrese el RUT: "))
            deuda = int(input("Ingrese la deuda en pesos: "))
            deudores[rut] = deuda
            break
        except ValueError:
            print("Por favor, ingrese números válidos para el RUT y la deuda.")

print("Ingrese el RUT de la persona y el monto del abono. Para finalizar, presione Enter sin ingresar un RUT.")
while True:
    rut_input = input("Ingrese el RUT de la persona: ")
    if rut_input == "":
        break
    try:
        rut = int(rut_input)
        if rut in deudores:
            abono = int(input("Ingrese el monto del abono: "))
            deudores[rut] -= abono
            if deudores[rut] <= 0:
                del deudores[rut]
        else:
            print("El RUT ingresado no está en la lista de deudores.")
    except ValueError:
        print("Por favor, ingrese un número válido para el RUT.")

print("Personas que quedaron deudoras y sus respectivos saldos de deuda:")
for rut, deuda in deudores.items():
    print(f"RUT: {rut}, Deuda: {deuda}")