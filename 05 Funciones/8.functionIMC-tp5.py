def calculate_bmi(weight_kg, height_m):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        weight_kg (int o float): El peso en kilogramos.
        height_m (int o float): La altura en metros.

    Returns:
        float: El valor del IMC, o None si la altura es cero o negativa.
    """
    if height_m <= 0:
        print("Error: La altura debe ser un valor positivo.")
        return None
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Solicitar al usuario los datos y mostrar el resultado
try:
    user_weight = float(input("Ingrese su peso en kilogramos (ej. 70.5): "))
    user_height = float(input("Ingrese su altura en metros (ej. 1.75): "))

    calculated_bmi = calculate_bmi(user_weight, user_height)

    if calculated_bmi is not None:
        print(f"\nSu Índice de Masa Corporal (IMC) es: {calculated_bmi:.2f}")
except ValueError:
    print("Entrada no válida. Por favor, asegúrese de ingresar números para peso y altura.")