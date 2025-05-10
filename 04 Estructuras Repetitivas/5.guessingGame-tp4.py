import random as rand

randomNumber = rand.randint(0,9)
counter = 0
userNumber = int(input("Ingrese un número del 0-9 hasta adivinar el correcto: "))
while userNumber != randomNumber:
    counter += 1
    userNumber = int(input("INCORRECTO!! - Ingrese un número del 0-9 hasta adivinar el correcto: "))

print(f"CORRECTO!!. El número era: {randomNumber}. Te llevó {counter} intentos adivinar")