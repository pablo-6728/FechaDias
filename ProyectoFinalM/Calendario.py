#Calendario que dice que dia cayo una fecha del calendario gregoriano

day = 0
month = 0
year = 1583

menu = 1

#Si I es 0, el día cae en Domingo; si I es 1, el día cae en Lunes; si I es 2, el día cae en Martes, etc

def calculoDia(dia, mes, ano):
    A = int((14 - mes)/12)           #A es el cociente de la división de 14 menos el mes entre 12,
    B = int(ano - A)                 #B es el año menos A
    C = int(mes + 12*A - 2)          #C es el mes más doce veces A menos 2
    D = int(B/4)                     #D es el cociente de la división de B entre 4
    E = int(B/100)                   #E es el cociente de la división de B entre 100
    F = int(B/400)                   #F es el cociente de la división de B entre 400
    G = int(31*C/12)                 #G es el cociente de 31 veces C entre 12
    H = int(dia + B + D - E + F + G) #H es el dia más B más D menos E más F más G
    I = (H % 7)                 #I es el resto de la división de H entre 7
    print(A, B, C, D, E, F, G, H, I)
    return (I)

while year >= 1583 and menu != 0:
    try:
        day = int(input("Escriba el numero de dia: "))
        month = int(input("Escriba el numero del mes: "))
        year = int(input("Ingrese un numero de ano (Mayor a 1582): "))

        if year < 1583:
            print("LE HE PEDIDO UN ANO MAYOR A 1583!")
            year = 1583

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


