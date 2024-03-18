def lenp (frase):
    r=frase.split("")
    l=list(map(len,r))
    print("La longitud de la paraula de la frase {} és {}".format(frase, l))

#Pprincipal
    
frase=input("Escriu una frase")
lenp(frase)