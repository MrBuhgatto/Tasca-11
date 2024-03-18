def ajuntar(l,d,c):
    a=[]
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
    print("La unio de les llistes es {}".format(a))

l=['Super','Hiper','Mini','Maxi']
d=['women','bole','mouse','bon']
ajuntar(l,d," ")
