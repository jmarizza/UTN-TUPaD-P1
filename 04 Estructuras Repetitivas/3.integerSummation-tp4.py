# Pido dos números al usuario
digit1 = int(input("Ingrese el primer número: "))
digit2 = int(input("Ingrese el segundo número: "))

# Valido que dígito es el mejor, si están invertidos. Los acomodo.
if digit1 > digit2:
    digit1, digit2 = digit2, digit1  # Intercambiar si están en orden inverso

suma = 0

# Sumo los valores entre digit1 y digit2 (excluyendo ambos)
for i in range(digit1 + 1, digit2):
    suma += i

print(f"La suma de los enteros entre {digit1} y {digit2}, excluyéndolos, es: {suma}")