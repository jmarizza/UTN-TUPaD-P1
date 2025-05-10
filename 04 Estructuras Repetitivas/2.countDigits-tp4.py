digit = int(input("Ingrese un número entero: "))
counter = 0

# Positivizo el input calculado el valor absoluto
digit = abs(digit)

# Si se ingresa un cero, el dígito es 1.
if digit == 0:
    counter = 1
else:
    while digit > 0:
        digit //= 10  # Divido hasta llegar a cero
        counter += 1 # Cuento cada ciclo en que dividí

print(f"El número tiene {counter} dígitos.")