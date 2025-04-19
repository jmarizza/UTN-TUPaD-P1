#Ejercicio7

numberA = int(input("Ingrese el primer número:"))
while numberA == 0:
    numberA = int(input("El número debe ser distinto de cero.\nIngrese nuevamente:"))
else:
    numberB = int(input("Ingrese el segundo número:"))
    while numberA == numberB or numberB == 0:
        numberB = int(input("Los números no pueden ser iguales.\nIngrese nuevamente el segundo número:"))
    else:
        for i in range(0,4):
            #Suma
            if i == 0:
                result = numberA + numberB
                print(f"El resultado de suma entre {numberA} y {numberB} es: {result}")
            #Resta
            elif i == 1:
                result = numberA - numberB
                print(f"El resultado de resta entre {numberA} y {numberB} es: {result}")
            #Producto
            elif i == 2:
                result = numberA * numberB
                print(f"El resultado del producto entre {numberA} y {numberB} es: {result}")
            #Division
            elif i == 3:
                result = numberA / numberB
                print(f"El resultado de la division entre {numberA} y {numberB} es: {result}")