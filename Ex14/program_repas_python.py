from functools import reduce
def menu_principal():
    opcio=0
    while opcio<1 or opcio>5: 
        print("""
          Menu principal:
          1. Programació estructurada
          2. Programació funcional
          3. Programació orientada a objectes
          4. Accés a fitxer
          5. Sortir
          """)
        opcio = int(input("Selecciona l'opció que vulgui executar: "))
        if opcio<1 or opcio>5:
            print("Opcio no vàlida, torna a provar")
        else:
            return opcio


def programacio_estructurada():
    print("Molt be has entrat a la programació estructurada!")
    l =("Pere","Pau","Paula","Puri","Polonia")
    x=list(map(lambda x: len(x)>4,l))
    print(x)
def programacio_funcional():    
    print("Molt be has entrat a la programació funcional")
    a = [1, 5, 7, 9]
    c = ["Hola, soc en ", "Joan i ", "avui no he sopat"]
    b = reduce(lambda x,y: x+y,c)
    print(b)
    d = ["Super", "Hiper", "Cata", "Mini", "Chachi"]
    e = ["Woman", "Loop", "Crack", "Mouse", "Piruli"]
    f = list(zip(d,"-",e))
    print(f)
def programacio_objectes():
    print("Molt be has entrat a la programació orientada a objectes")
def acc_fitxers():
    print("Molt be has entrat a l'accés als fitxers")
def sortir():
    print("Has sortit")
#Pprincipal
op=1
while op != 5:
    op = menu_principal()
    match (op):
        case 1: 
            programacio_estructurada()
        case 2: 
            programacio_funcional()
        case 3: 
            programacio_objectes()
        case 4: 
            acc_fitxers()
        case 5: 
            sortir()
        case other:
            print("Opcio no valida")