#Calendario que dice que dia cayo una fecha del calendario gregoriano

day = 0
month = 0
year = 1583

menu = 1

def calculoDia(day, month, year):
    A = (14 - month)/12
    B = year - A
    C = month + 12*A - 2
    D = B/4
    E = B/100
    F = B/400
    G = (C*31)/12
    H = day + B + D - E + F + G
    I = H % 7
    print(I)
    return (I)

while year >= 1583 and menu != 0:
    try:
        day = int(input("Escriba el numero de dia(1-31): "))
        month = int(input("Escriba el numero del mes (1-12): "))
        year = int(input("Ingrese un numero de ano (Mayor a 1582): "))

        if year < 1583:
            print("LE HE PEDIDO UN ANO MAYOR A 1583!")
            year = 1583

        elif month == 2 and day > 29 and year%4 == 0:
            print("Su ano es viciesto y su dia de febrero no puede ser mayor a 29")

        elif month == 2 and day > 28 and not(year%4 == 0):
            print("Su ano es viciesto y su dia no puede ser mayor a 28")

        elif month != 2 and day > 31:
            print("Su numero es mayor a 31 y no existen meses con mas de 31 dias, lo siento")

        elif month > 12:
            print("No hay mas de 12 meses")


        else:
            nuestro_dia = calculoDia(day, month, year)

#Verificacion del dia

        if nuestro_dia == 0:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Domingo")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 1:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Lunes")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 2:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Martes")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 3:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Miercoles")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 4:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Jueves")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 5:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Viernes")
            menu = int(input("Si desea terminar presione 0: "))

        elif nuestro_dia == 6:
            print("El dia " + str(day) + " del mes " +str(month) +" del ano " + str(year) + " cae un Sabado")
            menu = int(input("Si desea terminar presione 0: "))


    except:
        print("Error! Prueba otra vez")


