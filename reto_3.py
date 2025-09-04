pacientes = int(input("¿Cuántos pacientes hay? "))

contarHB = contarHN = contarHA = 0 
contarMB = contarMN = contarMA = 0  
sumarHB = sumarHN = sumarHA = 0.0
sumarMB = sumarMN = sumarMA = 0.0
tabla_auxiliar = [] 

for i in range(pacientes):
    genero = int(input("Digite 1 si es hombre o 2 si es mujer: "))
    hemoglobina = float(input("Digite su nivel de hemoglobina: "))

    tabla_auxiliar.append((genero, hemoglobina))

    if genero == 1: 
        if hemoglobina < 12.2:
            contarHB += 1
            sumarHB += hemoglobina
        elif 12.2 <= hemoglobina <= 16.6:
            contarHN += 1
            sumarHN += hemoglobina
        else:
            contarHA += 1
            sumarHA += hemoglobina

    elif genero == 2:  
        if hemoglobina < 12.6:
            contarMB += 1
            sumarMB += hemoglobina
        elif 12.6 <= hemoglobina <= 15:
            contarMN += 1
            sumarMN += hemoglobina
        else:
            contarMA += 1
            sumarMA += hemoglobina
    else:
        print("Género no válido, se ignora este registro.")

totalH = contarHB + contarHN + contarHA
totalM = contarMB + contarMN + contarMA

if totalH > 0:
    promedioH = (sumarHB + sumarHN + sumarHA) / totalH
else:
    promedioH = 0

if totalM > 0:
    promedioM = (sumarMB + sumarMN + sumarMA) / totalM
else:
    promedioM = 0

HombresArriba = HombresAbajo = HombresIgual = 0
MujeresArriba = MujeresAbajo = MujeresIgual = 0

for genero, hemoglobina in tabla_auxiliar:
    if genero == 1: 
        if hemoglobina > promedioH:
            HombresArriba += 1
        elif hemoglobina < promedioH:
            HombresAbajo += 1
        else:
            HombresIgual += 1
    elif genero == 2: 
        if hemoglobina > promedioM:
            MujeresArriba += 1
        elif hemoglobina < promedioM:
            MujeresAbajo += 1
        else:
            MujeresIgual += 1


print("\n--- RESULTADOS ---")
print(f"Promedio hombres: {promedioH}")
print(f"Promedio mujeres: {promedioM}")
print("Hombres arriba:", HombresArriba)
print("Hombres abajo:", HombresAbajo)
print("Hombres igual:", HombresIgual)
print("Mujeres arriba:", MujeresArriba)
print("Mujeres abajo:", MujeresAbajo)
print("Mujeres igual:", MujeresIgual)
