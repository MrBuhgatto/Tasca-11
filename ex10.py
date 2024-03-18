def div(a,b):
    

    try:
        c= a/b
        print("La divisio de {} i {} és {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segon paràmetre de la divisió no pot ser 0")

#Pprincipal
a= int(input("Introdueix un nombre: "))
b= int(input("Introdueix un nombre: "))
c= div(a,b)