zonas = int(input("¿Cuántas zonas desea analizar? "))

contarNA = contarMA = contarMO = contarSA = 0


mejores = []
peores = []

def clasificar_materia(valor):
    if valor > 5:
        return "sumamente apto"
    elif 4 < valor <= 5:
        return "moderadamente apto"
    elif 3 <= valor <= 4:
        return "marginalmente apto"
    else:
        return "no apto"

def clasificar_p2o5(valor):
    if valor > 69:
        return "sumamente apto"
    elif 57 <= valor <= 69:
        return "moderadamente apto"
    elif 46 <= valor < 57:
        return "marginalmente apto"
    else:
        return "no apto"

def peor_categoria(cat1, cat2):
    orden = ["no apto", "marginalmente apto", "moderadamente apto", "sumamente apto"]
    return cat1 if orden.index(cat1) < orden.index(cat2) else cat2


for z in range(zonas):
    print(f"\nZona {z+1}:")
    materia = list(map(float, input("Digite los 7 valores de materia orgánica separados por espacio: ").split()))
    p2o5 = list(map(float, input("Digite los 7 valores de P2O5 separados por espacio: ").split()))

    conteo_zona = {"no apto": 0, "marginalmente apto": 0, "moderadamente apto": 0, "sumamente apto": 0}

    for i in range(7):
        cat_m = clasificar_materia(materia[i])
        cat_p = clasificar_p2o5(p2o5[i])
        final = peor_categoria(cat_m, cat_p)

        conteo_zona[final] += 1


        if final == "no apto": contarNA += 1
        elif final == "marginalmente apto": contarMA += 1
        elif final == "moderadamente apto": contarMO += 1
        else: contarSA += 1

    max_val = max(conteo_zona.values())
    candidatas_max = [k for k, v in conteo_zona.items() if v == max_val]
    orden = ["no apto", "marginalmente apto", "moderadamente apto", "sumamente apto"]
    mejor = max(candidatas_max, key=lambda x: orden.index(x))
    mejores.append(mejor)

    min_val = min(conteo_zona.values())
    candidatas_min = [k for k, v in conteo_zona.items() if v == min_val]
    peor = max(candidatas_min, key=lambda x: orden.index(x))
    peores.append(peor)

print("RESULTADOS")
print("No apto:", contarNA)
print("Marginalmente apto:", contarMA)
print("Moderadamente apto:", contarMO)
print("Sumamente apto:", contarSA)

print("\nCategoría más frecuente en cada zona:", ", ".join(mejores))

print("Categoría menos frecuente en cada zona:", ", ".join(peores))

