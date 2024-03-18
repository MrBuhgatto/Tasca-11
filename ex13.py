class Animal():
    def __init__(self,atribut,edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print("Soc un animal")
class Cavall(Animal):
    def xerrar(self):
        print("Ííííí")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un Cavall")
class Dofi(Animal):
    def xerrar(self):
        print("IchIchIch")
    def mourem(self):
        print("Em moc nadant")
    def quisoc(self):
        print("Soc un Dofí")
class Abella(Animal):
    def xerrar(self):
        print("Sssssss")
    def mourem(self):
        print("Em moc volant")
    def quisoc(self):
        print("Soc una Abella")
    def picadura(self):
        print("Si m'emprenyes et picare")
class Huma(Animal):
    def __init__(self, nom, atribut, edat):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola")
    def mourem(self):
        print("Em moc caminant")
    def quisoc(self):
        print("Soc un Humà")
class Centaure(Huma, Cavall):
    def xerrar(self):
        print("Hola")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un Centaure")
class Fiet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeeeeee")
    def mourem(self):
        print("Em moc gatetjant")
    def quisoc(self):
        print("Soc un Fiet")
    def nompares(self):
        for e in self.pares:
            print(e.nom)
class Xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Soc un Xou")

#Pprincipal
        
a = [Cavall("Marro","4"), 
     Dofi("Gris","10"), 
     Abella("Negre i groga","0,5"), 
     Huma("Sibila", "Cristia", "7"), 
     Centaure("Fiona", "Marron","18"), 
     Fiet("Jordi","Moreno","9",["Fiona i Marc"]), 
     Xou("xou") ]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()