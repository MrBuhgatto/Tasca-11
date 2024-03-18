import os

companys=["Claudia","Clara","Paula","Joan","Marc","Ian","Sergi","Sebas","Anas","Hugo","Oscar","Josep","Fede","Alvaro","Joselu","Ayoub","David"]
os.mkdir("home/cicles/AO/Tasca-11/Prova")
os.chdir("home/cicles/AO/Tasca-11/Prova")
with open("/home/cicles/AO/Tasca-11/ex12.txt", "w") as f:
    print("Fitxer creat correctament!")
    for e in companys:
        f.write(e+"\n")
professors= ["David","Pep","Fela","Lluis","Joan"]
with open ("/home/cicles/AO/Tasca-11/ex12.txt","a+") as f:
    for e in professors:
        f.write(e+"\n")
a= []
with open("/home/cicles/AO/Tasca-11/ex12.txt", "r") as f:
    for e in f:
        c= e.split("\n")
        a.append(c[0])
print(a)