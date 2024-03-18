#Crear una funció que permeti llegir la informació d’un fitxer, però que controli que el fitxer existeix i que la seva obertura no doni cap problema. 
#Fes-ho també utilitzant with. Si voleu podeu practicar el try, except afegint-ho a les funcions anteriors.
def imprimir_fitxer(m):
    a= []
    with open(m, "r") as f:
        for e in f:
            c = e.split("\n")
            a.append(c[0])
    print(a)


def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")
    
#Pprincipal
    
fitxer = "/home/cicles/AO/Tasca-11/pipsas.txt"
llista = ["Federic", "Paula", "Pepe", "Marc", "Anas", "Sergi", "Ian", "Jordi", "Oscar"]
afegir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)