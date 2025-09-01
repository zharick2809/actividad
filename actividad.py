Genero_1 = 1  
Genero_2 = 2  

genero = int(input("Digite 1 si es Masculino / Digite 2 si es Femenino: "))
hemoglobina = float(input("Digite su nivel de Hemoglobina: "))


if genero == Genero_1:  
    if hemoglobina < 12.2:
        print("Su Hemoglobina es baja")
    elif 12.2 <= hemoglobina <= 16.6:
        print("Su Hemoglobina es normal")
    else:
        print("Su Hemoglobina es alta")

elif genero == Genero_2: 
    if hemoglobina < 12.6:
        print("Su Hemoglobina es baja")
    elif 12.6 <= hemoglobina <= 15:
        print("Su Hemoglobina es normal")
    else:
        print("Su Hemoglobina es alta")

else:
    print("No es posible generar la alerta")