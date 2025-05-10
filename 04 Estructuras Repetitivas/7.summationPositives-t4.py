number = int(input("Por favor ingrese un número entero positivo: "))

while (number <= 0):
    print ("ERROR - EL NÚMERO INGRESADO ES INCORRECTO.")
    number = int(input("Ingrese nuevamente un número entero positivo: "))
counter = 0
for i in range(0,number+1):
    counter += i

print(f"La sumatoria de los números comprendidos entre 0 y {number} es: {counter}")