def basic_operations(num1, num2):
    """
    Realiza suma, resta, multiplicación y división entre dos números.

    Args:
        num1 (int o float): El primer número.
        num2 (int o float): El segundo número.

    Returns:
        tuple: Una tupla con (suma, resta, multiplicacion, division).
               La división será None si el segundo número es cero.
    """
    sum_result = num1 + num2
    subtraction_result = num1 - num2
    multiplication_result = num1 * num2
    division_result = None
    if num2 != 0:
        division_result = num1 / num2
    else:
        print("Advertencia: No se puede dividir por cero.")
    return (sum_result, subtraction_result, multiplication_result, division_result)

# Demostración de la función
try:
    first_num = float(input("Ingrese el primer número para las operaciones: "))
    second_num = float(input("Ingrese el segundo número para las operaciones: "))

    results = basic_operations(first_num, second_num)

    print(f"\nResultados de las operaciones básicas con {first_num} y {second_num}:")
    print(f"Suma: {results[0]}")
    print(f"Resta: {results[1]}")
    print(f"Multiplicación: {results[2]}")
    if results[3] is not None:
        print(f"División: {results[3]:.2f}")
except ValueError:
    print("Entrada no válida. Por favor, ingrese solo números.")