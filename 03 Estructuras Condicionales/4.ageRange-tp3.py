#Armo mi funcion para ver rango etario y dejarla genérica para todo el proyecto
def ageRange(age):
    if not isinstance(age,int):
        raise TypeError("Solo se permiten valores enteros.")
    elif age <= 0:
        return("ERROR: La edad debe ser mayor a cero.")
    elif age < 12:
        return("Niño/a")
    elif age >= 12 and age < 18:
        return("Adolescente")
    elif age >= 18 and age < 30:
        return("Adulto/a joven.")
    else:
        return("Adulto/a")

# Pido datos y llamo función para conocer rango etario    
age = int(input("Ingrese una edad para evaluar rango etario de la persona: "))
print(f"De acuerdo a la edad ingresada. La persona es: {ageRange(age)}")