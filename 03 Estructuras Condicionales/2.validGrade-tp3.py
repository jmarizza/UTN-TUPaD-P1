#Solicito datos y valido que ingresen valores decimales positivos
try:

    grade = float(input("Ingrese la nota del alumno: "))

    if grade < 0:
        print("La nota ingresada debe ser igual o mayor a cero.")
    elif grade >= 6:
        print("APROBADO")
    else:
        print("DESAPROBADO")
        
except ValueError:
    raise TypeError("La nota ingresada debe ser un valor decimal.")