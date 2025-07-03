def multiplication_table(number):
    """
    Imprime la tabla de multiplicar de un número del 1 al 10.

    Args:
        number (int o float): El número del cual se imprimirá la tabla.
    """
    print(f"\n--- Tabla de multiplicar del {number} ---")
    for i in range(1, 11): # Itera del 1 al 10
        print(f"{number} x {i} = {number * i}")
    print("---------------------------------")

# Solicitar al usuario el número
try:
    input_number = float(input("Ingrese un número para ver su tabla de multiplicar: "))
    multiplication_table(input_number)
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número.")