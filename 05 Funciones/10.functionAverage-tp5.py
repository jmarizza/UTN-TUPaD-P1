def calculate_average(num_a, num_b, num_c):
    """
    Calcula el promedio de tres números.

    Args:
        num_a (int o float): El primer número.
        num_b (int o float): El segundo número.
        num_c (int o float): El tercer número.

    Returns:
        float: El promedio de los tres números.
    """
    average = (num_a + num_b + num_c) / 3
    return average

# Solicitar los números al usuario y mostrar el resultado
try:
    first_number = float(input("Ingrese el primer número: "))
    second_number = float(input("Ingrese el segundo número: "))
    third_number = float(input("Ingrese el tercer número: "))

    calculated_average = calculate_average(first_number, second_number, third_number)
    print(f"\nEl promedio de {first_number}, {second_number} y {third_number} es: {calculated_average:.2f}")
except ValueError:
    print("Entrada no válida. Por favor, ingrese solo números.")