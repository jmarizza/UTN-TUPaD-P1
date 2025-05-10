even = 0
odd = 0
positives = 0
negatives = 0

for i in range (0,100):
    while True:
        try:
            number = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número entero válido (sin decimales).")
    if number >= 0:
        positives += 1
    else:
        negatives += 1

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Los resultados son: \nPositivos = {positives}\nNegativos = {negatives}\nPares = {even}\nImpares = {odd}")
    