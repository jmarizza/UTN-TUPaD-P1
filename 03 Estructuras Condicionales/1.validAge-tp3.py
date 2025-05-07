#Solicito datos y valido que ingresen valores enteros positivos
try:

    age = int(input("Ingrse la edad a evaluar: "))

    if age <= 0:
        print("La edad ingresada deber ser mayor a cero. Ingrese una edad válida.")
    elif age > 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")
        
except ValueError:
    raise TypeError("La edad debe ser un valor entero.")