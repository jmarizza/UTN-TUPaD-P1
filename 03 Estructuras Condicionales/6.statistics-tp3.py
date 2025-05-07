import statistics as stat
import random

randomNumbers = [random.randint(1, 100) for i in range(50)]
mean = stat.mean(randomNumbers)
median = stat.median(randomNumbers)
modas = stat.multimode(randomNumbers)

# Tomamos la primera moda (aunque puede haber más)
mode = modas[0] if modas else None

# Mostrar valores
print(f"Números: {randomNumbers}")
print(f"Media: {mean}, Mediana: {median}, Moda: {mode}")

# Determinar sesgo
if mode is None:
    print("No se pudo calcular la moda.")
elif mean > median and median > mode:
    print("Sesgo positivo")
elif mean < median and median < mode:
    print("Sesgo negativo")
elif mean == median == mode:
    print("Sin sesgo")
else:
    print("Asimetría leve o ambigua")

#Podría haber generado tambien una funcion que devuelva el sesgo, pero lo deje asi como lo propone el ejercicio