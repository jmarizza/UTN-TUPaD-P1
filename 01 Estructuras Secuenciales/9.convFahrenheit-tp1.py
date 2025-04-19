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