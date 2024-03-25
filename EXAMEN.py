def menu():
    op=0
    while op<1 or op>14:
        print("""
        Programa principal
              1. Estructures condicionals, if
              2. Estructures condicionals, match
              3. Estructures iteratives, for e in b
              4. Estructures iteratives, for i in range(x)
              5. Estructures iteratives, for i,e in range(x)
              6. Funció de paràmetres
              7. Funció lambda
              8. Funció list comprehension
              9. Funció map
              10. Funció zip
              11. Funció filter
              12. Classes i objectes
              13. Fitxers
              14. Sortir
            """)
        op=int(input("Introdueixi una opció: "))
        if op<1 or op>14:
            print("Opció no vàlida, torni a elegir una opció \n")
        else:
            return op
        
def ex1():
    a= int(input("Introdueix un nombre: "))
    b= int(input("Introdueix un altre nombre: "))
    if a>b:
        print("{} és major que {}".format(a,b))
    elif b>a:
        print("{} és major que {}".format(b,a))
    else:
        print("Els dos son iguals")


def ex2():
    vocal=input("Introdueix una voacl: ")
    match(vocal):
        case 'a':
            print("La vocal introduïda és una a")
        case 'e':
            print("La vocal introduïda és una e")
        case 'i':
            print("La vocal introduïda és una i")
        case 'o':
            print("La vocal introduïda és una o")
        case 'u':
            print("La vocal introduïda és una u")
        case other:
            print("Opció no vàlida!")

def ex3():
    a= []
    b= []
    for i in range(3):
        a.append(input("Introdueixi la paraula: "))
    for e in a:
        b.append(len(e))
    print("Les longituds de la llista {} són {}".format(a,b))


def ex4():
    for i in range(1,10,2):
        print(i)

def ex5():
    llista = [12,6,9,33,8]
    dic= {}
    for i,e in enumerate(llista):
        dic[i]=e
    print("De la llista {} hem creat el diccionari {}".format(llista,dic))

def ex6(l,c):
    b=[]
    for e in l:
        if c in e:
            b.append(e)
    print("De la llista {}, les següents {} contenen el caràcters {}".format(l,c,b))

def ex7():
    a=[4,19,7,2,12]
    b= list(map(lambda y: y+10,a))
    print(b)

def ex8():
    l=[12,9,15,6,3]
    a=[x**2 for x in l if x%2==1]
    print(a)

def ex9():
    l=["caca","examen","python","euro","si"]
    a= list(map(lambda x: x[::-1], l))
    print(a)

def ex10():
    l= [10,9,8,7,6]
    a= [5,4,3,2,1]
    b= list(zip(l,a))
    print(b)

def ex11():
    a=[12,6,3,9,11]
    b=list(filter(lambda y: y%2==1,a))
    print("La nova llista és {}".format(b))


class Ordinador():
    def __init__(self,tipus,pantalla):
        self.tipus=tipus
        self.pantalla=pantalla
    def getTipus(self):
        pass
    def getPantalla(self):
        pass

class Portatil(Ordinador):
    def getTipus(self):
        print("És un portàtil")
    def getPantalla(self):
        print("15")

class Tablet(Ordinador):
    def getTipus(self):
        print("És una tablet")
    def getPantalla(self):
        print("9")

class Servidor(Ordinador):
    def getTipus(self):
        print("És un servidor")
    def getPantalla(self):
        print("21")

class PC(Ordinador):
    def getTipus(self):
        print("És un PC")
    def getPantalla(self):
        print("27")

def ex12():
    a = [Portatil("És un portàtil","15"), Tablet("És una tablet","9"), Servidor("És un servidor","21"), PC("És un PC","27")]
    for e in a:
        e.getTipus()
        e.getPantalla()

def ex13():
    with open("/home/cicles/AO/ex20.txt","w") as f:
        for e in range(10):
            f.write(str(e)+"\n")
    with open("/home/cicles/AO/ex20.txt","r") as f:
        for i in f:
            print(i)
            
#Programa principal
op = 1
while op != 14:
    op=menu()
    match(op):
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            l=["hola","adeu","hello","bye","alt","baix"]
            c="a"
            ex6(l,c)
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()
        case 12:
            ex12()
        case 13:
            ex13()
        case 14:
            print("Programa acabat, que ho passi molt bé i gràcies per utilitzar-me!")
