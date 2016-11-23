import math
print("DAVID HERNANDEZ- MARIA FERNANDA TIBANTA")
print("Perimetro y area de las figuras geometricas")
print ("\n")
n=int(input("Ingrese el numero de lados de una figura geometrica: "))

def triangulo():
    print ("El numero de lados pertenece a un triangulo")
    print ("\n")
    print ("Perimetro del triangulo")
    l=int(input("Ingrese el valor del lado del triangulo: "))
    perimetro=l*3
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del triangulo")
    b=int(input("Ingrese la base del triangulo: "))
    h=int(input("Ingrese la altura del triangulo: "))
    area=(b*h)/2
    print ("Area igual a: ", area)
    creartxt ("TRIANGULO")
    grabartxt (perimetro, area, "TRIANGULO")

def cuadrado():
    print ("El numero de lados pertenece a un cuadrado")
    print ("\n")
    print ("Perimetro del cuadrado")
    l=int(input("Ingrese el valor del lado del cuadrado: "))
    perimetro=l*4
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del cuadrado")
    area=l**2
    print ("Area igual a: ", area)
    creartxt ("CUADRADO")
    grabartxt (perimetro, area, "CUADRADO")

def pentagono():
    print ("El numero de lados pertenece a un pentagono")
    print ("\n")
    print ("Perimetro del pentagono")
    l=int(input("Ingrese el valor del lado del pentagono: "))
    perimetro=l*5
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del pentagono")
    ap=int(input("Ingrese el valor del apotema del pentagono: "))
    area=(5*l*ap)/2
    print ("Area igual a: ", area)
    creartxt ("PENTAGONO")
    grabartxt (perimetro, area, "PENTAGONO")
    
def hexagono():
    print("Su figura es un hexagono")
    lado=int(input("Ingresa la longitud del lado del hexagono: "))
    apotema= math.sqrt((lado**2)-(lado/2)**2)
    perimetro=lado*6
    print("El perimetro del hexagono es: ",perimetro)
    area= (6*lado*apotema)/2
    print("El area del hexagono es: ",round(area,2))
    creartxt ("HEXAGONO")
    grabartxt (perimetro, area, "HEXAGONO")
    
def heptagono():
    print("su figura es un pentagono")
    lado=int(input("Ingresa la longitud del lado del heptagono: "))
    perimetro= 7*lado
    apotema=math.sqrt((lado**2)-(lado/2)**2)
    print("El perimetro del hentagono es: ",perimetro)
    area=(7*lado*apotema)/2
    print("El area del heptagono es: ",round(perimetro,2))
    creartxt ("HEPTAGONO")
    grabartxt (perimetro, area, "HEPTAGONO")
    
def octogono ():
    print("su figura es un octogono")
    lado=int(input("Ingresa la longitud del lado del octogono: "))
    perimetro=8*lado
    apotema=math.sqrt((lado**2)-(lado/2)**2)
    print("El perimetro del octogono es: ",perimetro)
    area=(4*lado*apotema)
    print("El area del octogono es: ",round(area,2))
    creartxt ("OCTOGONO")
    grabartxt (perimetro, area, "OCTOGONO")

def eneagono():
     print("su figura es un eneagono")
     lado=int(input("Ingresa la longitud del lado del eneagono: "))
     perimetro=9*lado
     apotema=math.sqrt((lado**2)-(lado/2)**2)
     print("El perimetro del eneagono es: ",perimetro)
     area=(perimetro*apotema)/2
     print("El area del eneagono es: ",round(area,2))
     creartxt ("ENEAGONO")
     grabartxt (perimetro, area, "ENEAGONO")

def decagono():
    print("El numero de lados pertence a un decagono")
    print ("Perimetro del pentagono")
    l=int(input("Ingrese el valor del lado del decagono: "))
    perimetro=l*10
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del pentagono")
    ap=int(input("Ingrese el valor del apotema del decagono: "))
    area=(perimetro*ap)/2
    print ("Area igual a: ", area)
    creartxt ("DECAGONO")
    grabartxt (perimetro, area, "DECAGONO")

    
def figuras ():
    if (n==3):
        triangulo()
    elif (n==4):
        cuadrado()
    elif (n==5):
        pentagono()
    elif n==6:
        hexagono()
    elif n==7:
        heptagono()
    elif n==8:
        octogono()
    elif n==9:
        eneagono()
    elif n==10:
        decagono()



def creartxt(nomfigura):
    nombre=nomfigura+".txt"
    archi=open(nombre,'w')
    archi.close()

def grabartxt(perimetro, area, nombre):
    print (perimetro,area)
    a=str (perimetro)
    b=str (area)
    archi=open(nombre+".txt",'a')
    archi.write ("El perimetro es: " + a +"\n")
    archi.write ("El area es: " + b +"\n")
    archi.close()


figuras()

