#Llegir 2 llistes i sumar cada element de la 1ª llista, per la suma de tots elements de la 2ª llista

def llegir_llista():
    a  = '1'
    l= []
    while a != '.':
        a = input("Introdueix un numero o element diferent a '.': ")
        if a != '.':
            l.append(int(a))
        else:
            return l

def sumatori_llista(a):
    b = 0
    for e in a:
        b+= e
    return b

def sumar_llista(a,b):
    l= []
    for e in a:
        l.append(e+b)
    print("La suma de la llista l={} amb n={} és d={}".format(a,b,l))

#Programa principal
    
a = llegir_llista()
b = llegir_llista()
c = sumatori_llista(b)
sumar_llista(a,c)