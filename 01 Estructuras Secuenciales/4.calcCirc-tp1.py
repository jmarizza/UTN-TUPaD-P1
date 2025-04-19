#Ejercicio4
import math

radio = float(input(f"Ingrese el radio del círculo: "))
area = round((math.pi*(pow(radio,2))),2)
perimeter = round(2*math.pi*radio,2)

print(f"El área del circúlo es: {area}\nEl perímetro del círculo es: {perimeter}")