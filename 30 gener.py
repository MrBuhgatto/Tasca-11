l = [3,23,73]

#Per a cada element d'l el multiplica per a, a de llegir
a = int(input("Introdueix el nombre a multiplicar: "))
x= list(map(lambda x: x*a,l))

print(x)