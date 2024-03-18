from functools import reduce

def passar_a_numero(llista):
    a=list(map(lambda x: str(x), llista))
    b=reduce(lambda x,y: x+y,a)
    print("La llista {} és el número {}".format(llista,b))

#Pprincipal
l= [3,5,7,9,1]
passar_a_numero(l)