import statistics as stat

numbers = []

for i in range(0,100):
    while True:
        try:
            number = int(input("Ingrese un número a evaluar: "))
            break
        except ValueError:
            print("INCORRECTO - El valor ingresado debe ser un entero.")
            number = int(input("Ingrese un número a evaluar: "))
    numbers.append(number)

total = sum(numbers)
median = stat.mean(numbers)
print(f"El total de los número ingresados es de {total}\nLa media de los número ingresados es de: {median}")
    
    