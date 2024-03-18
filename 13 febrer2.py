"""
import json
with open("/home/cicles/AO/Tasca-11/prova.json") as f:
    dades=json.load(f)
    print(dades)
"""
"""
import json
#Escriure dades dins d'un fitxer .json

dades = {"nom":"Pere","cognom":"Pons","edat":"15"}
with open("ex2.json","w") as f:
    json.dump(dades,f)"""

from urllib import request
f = request.urlopen('https://core.ac.uk/download/pdf/52478597.pdf')
dades = f.read()
print(dades.decode('utf-8'))