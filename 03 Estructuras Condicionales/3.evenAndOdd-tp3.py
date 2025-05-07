#Armo funcion para validar tipo de dato que ingresan y dejarla genérica para todo el proyecto
def evenOdd (number):
    if not isinstance(number,(int,float)):
        raise TypeError("Solo se permiten valores numéricos enteros, o decimales.")
    elif number % 2 == 0:
        return ("PAR")
    else:
        return ("IMPAR")

number = float(input("Ingrese al número a evaluar: "))
print(f"El número {number} es un número: {evenOdd(number)}.")


