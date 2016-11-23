print ("Ecuacion cuadratica")
print ("Ecuacion= ax**2+bx+c")

def ecuacion():
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    c=int(input("Ingrese el valor de c: "))
    if (a<=0 ):
        print("el valor de a debe ser mayor a cero")
    else:
        dis=b**2-(4*a*c)
        if (dis<=0):
            print ("No existen raices negativas")
        if (dis>0):   
            raiz=dis**0.5
            resul2=(-b+raiz)/2*a
            resul3=(-b-raiz)/2*a
            #print ("El resultado es: ", resul2 ,"\t", resul3)        
            grabartxt(resul2,resul3)

def creartxt():
    archi=open('Resultado.txt','w')
    archi.close()

def grabartxt(resul2,resul3):
    print (resul2,resul3)
    a=str (resul2)
    b=str (resul3)
    archi=open('Resultado.txt','a')
    archi.write ("El resultado es: " + a + b)
    archi.close()


creartxt()
ecuacion()










      


