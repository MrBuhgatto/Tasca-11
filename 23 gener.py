#Llegir llista i multiplicar cada element per un numero donat

def llegir_llista():
    a  = '1'
    l= []
    while a != '.':
        a = input("Introdueix un numero o element diferent a '.': ")
        if a != '.':
            l.append(int(a))
        else:
            return l
        
def multiplicar(a,x):
    b=[]
    for e in a:
        b.append(e * x)
    print("La multiplicacio de cada element d'x={} per el num y={} és {}".format(a,x,b))

#Principal
l = llegir_llista()
n = int(input("Introdueix el nombre a multiplicar: "))
multiplicar(l,n)