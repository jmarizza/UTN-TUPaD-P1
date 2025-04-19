#Ejercicio6
number = int(input("Ingresa un número para conocer su tabla:"))
while number < 0:
    number = int(input("El número debe ser mayor o igual a cero. Integrese nuevamente:"))
else:
    for i in range(0, 11):
        result = number * i
        print(f"{number} * {i} = {result}")