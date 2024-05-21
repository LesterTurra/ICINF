e_500_900 = 0
e_mas_900 = 0
g_total = 0

while True:
    sueldo = float(input("Sueldo mensual (-1 para finalizar): "))
    if sueldo == -1:
        break
    g_total += sueldo
    if 500000 <= sueldo <= 900000:
        e_500_900 += 1
    elif sueldo > 900000:
        e_mas_900 += 1

print("Empleados ($500k - $900k):", e_500_900)
print("Empleados (>$900k):", e_mas_900)
print("Gasto total:", g_total)