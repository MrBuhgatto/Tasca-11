"""
with open("/home/cicles/AO/Tasca-11/fitxerpy.txt", "a") as f:
    for i in range(4,11):
        f.write(str(i)+"\n")"""
import csv
with open("/home/cicles/AO/Tasca-11/prova.csv", "r") as f:
    info = csv.reader(f)
    for linia in info:
        print(linia)