l = ['a','e','i','o','u']
a=input("Introdueix una cadena de caràcters: ")
b= a.lower()
x= list(filter(lambda x: x in b,l))

print("Les vocals son: {}".format(x))