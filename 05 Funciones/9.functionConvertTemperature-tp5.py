def celsius_to_fahrenheit(celsius_temp):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius_temp (int o float): La temperatura en grados Celsius.

    Returns:
        float: La temperatura equivalente en grados Fahrenheit.
    """
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

# Solicitar al usuario la temperatura en Celsius y mostrar el resultado
try:
    temp_celsius_input = float(input("Ingrese la temperatura en grados Celsius: "))
    temp_fahrenheit_output = celsius_to_fahrenheit(temp_celsius_input)
    print(f"{temp_celsius_input}°C equivalen a {temp_fahrenheit_output:.2f}°F.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número para la temperatura.")