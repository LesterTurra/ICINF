precios_clp=[]

for i in range (10):
    tasa_cambio_usd_clp=950.0

print("Ingrese 10 precios en en pesos chilenos:")

for i in range(10):
    precio=float(input("Ingrese un precio: "))
    precios_clp.append(precio)

precios_usd=[]
for precio_clp in precios_clp:
    precio_usd=precio_clp/tasa_cambio_usd_clp
    precios_usd.append(precio_usd)

print("Lista completa de precios en USD: ")
print(["$"+"%.2f"%precio_usd for precio_usd in precios_usd ])  