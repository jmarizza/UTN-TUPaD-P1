#Defino función para ver si termina en vocal
def isVowel(word):
    if not isinstance(word,str):
        raise TypeError("Debe pasarse un string.")
    elif word[-1].upper() in ('A','E','I','O','U',"Á","É","Í","Ó","Ú"):
        return(word+ "!")
    else:
        return(word)
#Solicito datos y llamo función    
word = input("Ingresa el texto a evaluar: ")
print(f"Tu texto formateado es: {isVowel(word)}")