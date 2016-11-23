print ("Ecuacion cuadratica")
print ("Ecuacion= ax**2+bx+c")

def ecuacion():
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    c=int(input("Ingrese el valor de c: "))
    if (a<=0 ):
        print("el valor de a debe ser mayor a cero")
    elif (a>0):
        resul1=b**2-(4*a*c)
        raiz=resul1**0.5
        resul2=(-b+raiz)/2*a
        resul3=(-b-raiz)/2*a
        print ("El resultado es: ", resul2 ,"\n", resul3)        


ecuacion()






      


