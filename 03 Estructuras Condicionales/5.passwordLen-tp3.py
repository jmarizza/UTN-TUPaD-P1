# Defino mi función para calcular largo y validar tipo de dato y dejarla genérica para todo el proyecto
def lenPwd(pwd):
    if not isinstance(pwd,str):
        raise TypeError("Solo se admiten datos tipo char")
    elif len(pwd) >= 8 and len(pwd) <= 14:
        return True
    else:
        return False
# Controlo, si la función retorna FALSE. Vuelvo a pedir pwd    
while True:
    pwd = input("Ingrese su contraseña: ")
    if lenPwd(pwd):
        print("La contraseña ingresada es correcta.")
        break
    else:
        print("Por favor ingrese una contraseña entre 8 y 14 caracteres")



