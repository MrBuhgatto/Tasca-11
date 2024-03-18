def f(n):
    return lambda a: a*n

doble=f(2)
triple=f(3)
deu=f(10)
a= triple(10)

print(a)

x = reduce(lambda a,b: a.join(b),l)