d = {"Tasca 1": 7, "Tasca 3": 8, "Tasca 7": 10}
l = d.items() #passa a llista
y = dict(sorted(l,key=lambda x:x[1], reverse=True)) # reverse=True els ordena de major a menor
print(y)
