#Se solicita el nombre a convertir.
name = input("Ingrese su nombre: ")

#Armo menú para el usuario.
print(
    "=== Menú ===\n"
    "1. Si quiere su nombre en mayúsculas.\n"
    "2. Si quiere su nombre en minúsculas.\n"
    "3. Si quiere su nombre con la primera letra mayúscula \n"
    "4. Para salir."
)

#Solicito y leo opción.
option = int(input("Ingrese una opción (1-3): "))

#Evalúo opción y formateo el texto.
if option == 1:
    print(f"Su nombre en mayúsculas es: {name.upper()}")

elif option == 2:
    print(f"Su nombre en minúsculas es: {name.lower()}")
elif option == 3:
    print(f"Su nombre en título es: {name.title()}")
elif option == 4:
    print(f"Nos vemos!")
else:
    print(f"La opción ingresasa {option} es incorrecta.")
