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