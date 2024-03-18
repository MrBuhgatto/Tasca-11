#Llegir dues llistes de 5 elements cada una i sumarem els elements de la mateixa posició

def llegir_llista():
    l= []
    for e in range(5):
        l.append(int(input("Introdueix una llista de 5 elements: ")))
    return l
def sumar_elements(x,y):
    b = []
    for e in range(5):
        b.append(x[e]+y[e])
    print("La suma per posició entre les llistes '{}' i '{}' és '{}'".format(x,y,b))

#Programa principal
s = llegir_llista()
d = llegir_llista()
sumar_elements(s,d)

