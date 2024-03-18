a = [ 3, 4, 5, 6]
b = [ 7, 8, 11, 15]
c = [ 24, 355, 232]
print(sorted(list(zip(a,b,c)), lambda x:x[1],reverse=True))
