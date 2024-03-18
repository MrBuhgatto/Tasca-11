from functools import reduce
"""
#Parell
y = [x for x in range(0, 100) if x % 2 == 0]
print(y)

#Senar
y = [x for x in range(0, 100) if x % 2 == 1]
print(y)

#De tres en tres
y = [x for x in range(0, 100, 3)]
print(y)

#Elevant els nombres
y = [x**3 for x in range(0, 20) if x % 2 == 1]
print(y)
"""
y = [(x-1)**2 for x in range(-23, 75) if x % 2 == 0]
x = reduce(lambda x,y: x*y, y)
print(x)