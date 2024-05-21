def determinar_nivel():
    total = int(input("Ingrese el total de preguntas: "))
    correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
    
    porcentaje = (correctas / total) * 100
    porcentaje = int(porcentaje * 100) / 100.0
    
    if porcentaje >= 95:
        nivel = "Nivel máximo"
    elif porcentaje >= 70:
        nivel = "Nivel medio"
    elif porcentaje >= 40:
        nivel = "Nivel regular"
    else:
        nivel = "Fuera de nivel"
    
    print("Porcentaje de respuestas correctas:", porcentaje, "%")
    print("Nivel:", nivel)

determinar_nivel()

