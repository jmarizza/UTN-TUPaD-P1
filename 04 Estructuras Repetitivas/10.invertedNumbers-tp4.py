while True:
    numberInput = input("Ingrese un número entero (positivo o negativo): ")
    if numberInput.lstrip('-').isdigit():
        break
    else:
        print("ERROR: Ingrese un número entero válido.")

isNegative = numberInput.startswith('-')
digitsOnly = numberInput.lstrip('-')

print(f"\nInvirtiendo los dígitos de: {digitsOnly}")
reversedDigits = ""

for i in range(len(digitsOnly) - 1, -1, -1):
    print(f"Agregando dígito: {digitsOnly[i]}")
    reversedDigits += digitsOnly[i]

if isNegative:
    reversedNumber = '-' + reversedDigits
else:
    reversedNumber = reversedDigits

print(f"\nEl número invertido es: {reversedNumber}")
