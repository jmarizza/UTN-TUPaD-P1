#Defino función para obtener día y mes a partir de una fecha ingresada como string
def splitDate (inputDate):
    splitedDate = inputDate.split("/") #Divido la fecha en partes usando el caracter "/"

    #Verifico que se hayan obtenido exactamente dos partes (día y mes)
    if len(splitedDate) != 2:
        return(False)
    try:
        day = int(splitedDate[0]) #Intento convertir el día a entero
        month = int(splitedDate[1]) #Intento convertir el mes a entero

        #Verifico que el día y el mes estén dentro de un rango válido
        if not (1<= day <= 31 and 1<= month <= 12):
            return False
        return day, month #Devuelvo una tupla con día y mes si todo está bien
    except ValueError:
        return False #Si no se pudo convertir a entero, retorno False

#Defino función para calcular la estación del año según el hemisferio y la fecha
def calculateSeason (hemisphere,month,day):
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day <=20):
        season = 'VERANO'
    elif (month == 3 and day >= 21) or (4 <= month <= 5) or (month == 6 and day < 21):
        season = 'OTOÑO'
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 23):
        season = 'INVIERNO'
    else:
        season = 'PRIMAVERA'
        
    #Si el hemisferio es norte, se invierten las estaciones
    if hemisphere.upper() == 'N':
        opposite = {
            "INVIERNO": "VERANO",
            "VERANO": "INVIERNO",
            "PRIMAVERA": "OTOÑO",
            "OTOÑO": "PRIMAVERA"
        }
        season = opposite[season]
    elif hemisphere.upper() != 'S':
        return "El hemisferio ingresado es incorrecto." #Valido que el hemisferio sea correcto. Sino retorno mensaje informando.

    return season #Retorno la estación correspondiente


#Bucle para solicitar y validar la fecha ingresada
while True:
    userDate = input('Ingrese una fecha con formato "dd/mm": ')
    userSplitedDate = splitDate(userDate)
    
    if userSplitedDate:
        day, month = userSplitedDate
        break
    else:
        print("La fecha ingresada posee un formato incorrecto. Intente nuevamente")

while True:
    userHemisphere = input('Ingrese el hemisferio "N"/"S": ')
    if userHemisphere in ('N','S'):
        break
    else:
        print("El hemisferio ingresado es incorrecto. Intente nuevamente")

#Diccionario para convertir abreviaciones a palabras completas
hemispheres = {'N': 'NORTE', 'S':'SUR'}


#Imprimo el resultado final
print(f'Para la fecha {userDate}, en el hemisferio {hemispheres[userHemisphere]}. La estación del año es: {calculateSeason(userHemisphere,month,day)}')    


#Podía haber modularizo todo más aún, haciendo funciones para pedir la fecha y el hemisferio y otra main donde se llamen a las primeras. 
#Finalmente llamaría a la función main(). De esta forma tendría el código modularizado y sería escalable por si hay que agregarle llamado a APIS,
#interfaz, o inclusive armar tests sobre las funciones

