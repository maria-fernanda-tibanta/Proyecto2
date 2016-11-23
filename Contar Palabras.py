def creartxt():
    archi=open('Resultado palabras.txt','w')
    archi.close()

    
def leertxt():
    numero=0
    archi=open('Texto Animales.txt','r')
    linea=archi.readline()
    while linea !="":
        print (linea)
        linea=archi.readline()
        numero=len (linea) + numero
        #print(numero)
    grabartxt(numero)
    archi.close()



def grabartxt(numero):
    print(numero)
    a=str(numero)
    archi=open('Resultado palabras.txt','a')
    archi.write('El numero de caracteres que tiene el texto es: ' + a)
    archi.close()
    
creartxt()
leertxt()
