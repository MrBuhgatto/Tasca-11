def llegir_llista():
    b = []
    a = '1'
    while a!='.':
        a = input("Introdueixi un numero per posar a la llista: ")
        if a!='.':
            b.append(int(a))
        else:
            return b

def sumar_elements(x):
    sumatori=0
    for e in x:
        sumatori += e
    return sumatori

a = llegir_llista()
b = llegir_llista()
x = len(a)
y = len(b)
z = abs(x-y)
c = sumar_elements(a)
d = sumar_elements(b)
e = c + d