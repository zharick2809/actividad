contarHB = 0
contarHN = 0
contarHA = 0
contarMB = 0
contarMN = 0
contarMA = 0


Genero_1 = 1 
Genero_2 = 2 

Pacientes = int(input("Digite cuantos pacientes hay: "))

for _ in range(Pacientes):  
    genero = int(input("Digite 1 si es masculino / Digite 2 si es femenino: "))
    hemoglobina = float(input("Digite su nivel de hemoglobina: "))


    if genero == Genero_1:
        if hemoglobina < 12.2:
            print("Su hemoglobina es baja")
            contarHB += 1
        elif 12.2 <= hemoglobina <= 16.6:
            print("Su hemoglobina es normal")
            contarHN += 1
        elif hemoglobina > 16.6:
            print("Su hemoglobina es alta")
            contarHA += 1
        else:
            print("No es posible generar la alerta")

    elif genero == Genero_2:
        if hemoglobina < 12.2:
            print("Su hemoglobina es baja")
            contarMB += 1
        elif 12.2 <= hemoglobina <= 15:
            print("Su hemoglobina es normal")
            contarMN += 1
        elif hemoglobina > 15:
            print("Su hemoglobina es alta")
            contarMA += 1
        else:
            print("No es posible generar la alerta")

    else:
        print("No es posible generar la alerta")

print("Mujeres con hemoglobina baja:", contarMB)
print("Mujeres con hemoglobina normal:", contarMN)
print("Mujeres con hemoglobina alta:", contarMA)

print("Hombres con hemoglobina baja:", contarHB)
print("Hombres con hemoglobina normal:", contarHN)
print("Hombres con hemoglobina alta:", contarHA)