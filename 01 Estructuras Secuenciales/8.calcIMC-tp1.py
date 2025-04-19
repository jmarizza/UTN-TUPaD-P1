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