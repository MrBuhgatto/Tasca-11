def pot(p):
    r = [x**p for x in range(1,10)]
    print("Les potencies elevades a {} dels 10 primers numeros es {}".format(p,r))

#Pprincipal
p=int(input("Introdueixi un numero el qual voleu elevar a la resta: "))
pot(p)