number = int(input("Ingrese un número para sumar a la secuencia (0 para finalizar): "))
summation = 0
while number != 0:
    summation += number
    number = int(input("Ingrese otro número (0 para finalizar): "))
    print(f"El resultado la suma de secuencia es: {summation}")

print(f"El resultado final de la suma de secuencia es: {summation}")
