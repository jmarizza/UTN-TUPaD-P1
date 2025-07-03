def seconds_to_hours(seconds):
    """
    Convierte una cantidad de segundos a horas.

    Args:
        seconds (int o float): La cantidad de segundos a convertir.

    Returns:
        float: La cantidad de horas correspondientes.
    """
    hours = seconds / 3600  # Hay 3600 segundos en una hora
    return hours

# Solicitar al usuario los segundos
try:
    input_seconds = float(input("Ingrese la cantidad de segundos: "))
    calculated_hours = seconds_to_hours(input_seconds)
    print(f"{input_seconds} segundos equivalen a {calculated_hours:.2f} horas.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número para los segundos.")