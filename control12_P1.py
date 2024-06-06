puntajes = []

for dia in range(1, 16):
    puntaje = int(input(f"Ingrese el puntaje del día {dia}: "))
    puntajes.append(puntaje)

print("Días con puntaje menor a 70:")
for dia, puntaje in enumerate(puntajes, 1):
    if puntaje < 70:
        print(f"Día {dia}")

print("\nDías con puntaje mayor o igual a 70:")
for dia, puntaje in enumerate(puntajes, 1):
    if puntaje >= 70:
        print(f"Día {dia}")

puntajes = []

for dia in range(1, 16):
    puntaje = int(input(f"Ingrese el puntaje del día {dia}: "))
    puntajes.append(puntaje)

print("Días con puntaje menor a 70:")
for dia, puntaje in enumerate(puntajes, 1):
    if puntaje < 70:
        print(f"Día {dia}")

print("\nDías con puntaje mayor o igual a 70:")
for dia, puntaje in enumerate(puntajes, 1):
    if puntaje >= 70:
        print(f"Día {dia}")