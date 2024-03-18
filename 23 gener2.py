#Llegir una llista de 10 elements i a cada element lis sumam un numero donat

def llegir_llista():
    l= []
    for i in range(10):
        l.append(int(input("Introdueix una llista de 10 elements: ")))
    return l
def sumar_llista(a,b):
    l= []
    for e in a:
        l.append(e+b)
    print("La suma de la llista {} sumada per {} dona com a resultat {}".format(a,b,l))

#Principal
l=llegir_llista()
n=int(input("Introdueix un numero a sumar: "))
sumar_llista(l,n)

