l = [4,23,71,375]

#Per a cada element d'l el multiplica per a, a de llegir
x= list(filter(lambda x: x % 2 == 1,l))

print("Els nombres senars son: {}".format(x))