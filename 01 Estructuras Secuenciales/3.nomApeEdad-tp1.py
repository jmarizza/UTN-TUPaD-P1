#Ejercicio3
userData = []
for i in range(0,4):
    if i == 0:
        data = input(f"Ingresa tu nombre: ")
        userData.append(data)
    elif i == 1:
        data = input(f"Ingresa tu apellido: ")
        userData.append(data)
    elif i == 2:
        data = input(f"Ingresa tu edad: ")
        userData.append(data)
    elif i == 3:
        data = input(f"Ingresa tu lugar de residencia: ")
        userData.append(data)
print(f"Mi nombres es {userData[0]} {userData[1]}, tengo {userData[2]} años. Y mi lugar de residencia es {userData[3]}")