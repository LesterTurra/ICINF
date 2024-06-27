notas=[]
print("Ingresa las notas. (0 para finalizar): ")

while True:
    nota=float("Ingrese una nota : ")
    if nota == 0:
        break
    notas.append(nota)

cantidad_notas=len(notas)
if cantidad_notas>0:
    promedio_notas=sum(notas/cantidad_notas)
else:
    promedio_notas=0

notas_bajo_4=len([nota for nota in notas if nota<4.0])
notas_igual_o_mayor_4=len([nota for nota in notas if nota>=4.0])

print("1) cantidad de notas: ") 
print(cantidad_notas)
print("2) promedio de notas: ") 
print(promedio_notas)
print("3) cantidad de notas bajo nota 4.0: ") 
print(notas_bajo_4)
print("4) cantidad de notas igual o mayor que nota 4,0: ") 
print(notas_igual_o_mayor_4)


