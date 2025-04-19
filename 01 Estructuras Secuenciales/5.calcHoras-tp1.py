#Ejercicio5

seconds = int(input("Ingrese la cantidad de segundos: "))
while seconds <= 0:
    seconds = input("La cantidad de segundos debe ser mayor a 0. Ingrese la cantidad de segundos: ")
else:
    hours = round((seconds/3600),2)
    print(f"Se ingresaron: {seconds} segundos.\nEsto equivale a: {hours} horas")