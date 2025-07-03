def personal_data(name,sure_name,age,address):
    print(f"Mi nombre es {name}, mi apellido es {sure_name}, tengo {age} anios. Y vivo en {address}")


if __name__ == "__main__":
    name = input(f"Ingresa tu nombre: ")
    sure_name = input(f"Ingresa tu apellido: ")
    age = input(f"Ingresa tu edad: ")
    address = input(f"Ingresa tu direccion: ")
    
    personal_data(name, sure_name,age,address)