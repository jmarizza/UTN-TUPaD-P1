numeros = [8, 15 , 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# El algoritmo quita de la lista el elemento más grande. En este caso utiliza el operador "mayor que" (>) para evaluar. 
# Si fuesen string utilizaría el orden lexicográfico.
# Si no pudiese determinar el orden por tener valores mixtos arrojaría un error.
# Si no hubiese elementos en la la lista arrojaría error.