# REDUCE

from functools import reduce

m=[3,4,5]
s=reduce(lambda x,y: y+x,m)
print(s)