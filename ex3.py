def igual_inicial(x,a,b):
    l = list(filter(lambda y: y[0] == a or y[0] == b, x))
    return l

x = ["maria", "manta", "peu", "ma", "caca", "hola"]
a = "m"
b = "p"
print(igual_inicial(x,a,b))