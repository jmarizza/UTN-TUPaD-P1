#Ejercicio1
print("Hola mundo")


#Ejercicio2
name = input("Ingresa tu nombre: ")
print(f"Hola {name}!!")


#Ejercicio3
userData = []
for i in range(0,4):
    if i == 0:
        data = input(f"Ingresa tu nombre: ")
        userData.append(data)
    elif i == 1:
        data = input(f"Ingresa tu apellido: ")
        userData.append(data)
    elif i == 2:
        data = input(f"Ingresa tu edad: ")
        userData.append(data)
    elif i == 3:
        data = input(f"Ingresa tu lugar de residencia: ")
        userData.append(data)
print(f"Mi nombres es {userData[0]} {userData[1]}, tengo {userData[2]} años. Y mi lugar de residencia es {userData[3]}")


#Ejercicio4
import math

radio = float(input(f"Ingrese el radio del círculo: "))
area = round((math.pi*(pow(radio,2))),2)
perimeter = round(2*math.pi*radio,2)

print(f"El área del circúlo es: {area}\nEl perímetro del círculo es: {perimeter}")

#Ejercicio5

seconds = int(input("Ingrese la cantidad de segundos: "))
while seconds <= 0:
    seconds = input("La cantidad de segundos debe ser mayor a 0. Ingrese la cantidad de segundos: ")
else:
    hours = round((seconds/3600),2)
    print(f"Se ingresaron: {seconds} segundos.\nEsto equivale a: {hours} horas")

#Ejercicio6
number = int(input("Ingresa un número para conocer su tabla:"))
while number < 0:
    number = int(input("El número debe ser mayor o igual a cero. Integrese nuevamente:"))
else:
    for i in range(0, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

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

#Ejercicio8

#Defino mi función
def IMC(weight,height):
    if not isinstance(weight,(int,float)) or not isinstance(height,(int,float)):
        raise TypeError("Ambos parámetros deben ser númericos (enteros o decimales).")
    height = height/100 #Paso a metros la altura
    result = round(weight / pow(height,2),1)
    return(result)


#Valido que no ingresen caracteres
while True:
    try:
        weight = float(input("Ingrese su peso en kilogramos: "))
        height = float(input("Ingrese su altura en centímetros: "))
        break #Salgo del loop si todo está OK
    except ValueError:
        print("Solo pueden ingresarse valores numéricos. Intente nuevamente.")

#Llamo función y muestro mensaje
print(f"Su IMC es de: {IMC(weight,height)}")

#Ejercicio9
#Defino mi función para convertir a fahrenheit
def convTemp(temperature): 
    if not isinstance(temperature, (int, float)):
        raise TypeError("La temperatura debe ser entera o decimal.")
    fahrenheit = (temperature * 1.8) + 32
    return fahrenheit 


while True:
    try:
        temperature = float(input("Ingrese la temperatura que desee convertir: "))
        fahrenheit = convTemp(temperature)
        break
    except ValueError:
        print("La temperatura debe ingresarse como entero, o como decimal. Intente nuevamente.")

print(f"La temperatura {temperature} ºC, equivalen a: {fahrenheit} ºF")

#Ejercicio10

while True:
    try:
        number = 0
        for i in range(0,3):
            number += float(input(f"Ingrese el número Nº{i+1}: "))
        break        
    except ValueError:
        print("Solo puede ingresar valores numéricos enteros o decimales. Intente nuevamente.")
average = number/3
print(f"El promedio de los números ingresados es de: {average}")