#Función para calcular terremoto
def classifyEarthquake(magnitude):
    if magnitude < 3:
        return "Muy leve (imperceptible)."
    elif magnitude >= 3 and magnitude < 4:
        return "Leve (ligeramente perceptible)."
    elif magnitude >= 4 and magnitude < 5:
        return "Moderado (sentido por personas, pero generalmente no causa daños)."
    elif magnitude >= 5 and magnitude < 6:
        return "Fuerte (puede causar daños en estructuras débiles)."
    elif magnitude >= 6 and magnitude < 7:
        return "Muy Fuerte (puede causar daños significativos)."
    else:
        return "Extremo (puede causar graves daños a gran escala)."

# Programa principal
try:
    magnitude = float(input("Ingrese la magnitud del terremoto: "))
    result = classifyEarthquake(magnitude)
    print(f"Clasificación: {result}")
except ValueError:
    print("Por favor, ingrese un número válido.")