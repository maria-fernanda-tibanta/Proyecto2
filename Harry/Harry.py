print("CONTAR LAS VECES QUE SE REPITE UNA PALABRA EN UN TEXTO"," BY DAVID HERNANDEZ Y MARIA FERNANDA TIBANTA")
def contarTXT(archivo,palabra):
    cont=0
    numero=0
    archi=open(archivo,'r')
    linea=archi.readline()
    #print(linea.count(palabra))
    while linea !="":
        cont+=linea.count(palabra)
        #print (linea)
        
        linea=archi.readline()
    numero=cont
    print("La palabra ingresada: ",palabra," se repite: ",numero," veces en el texto")
    archi.close()
    
archivo=input("Ingrese el texto que desea abrir ejemplo(datos.txt): ")
palabra= input("Ingrese la palabara que desea buscar en el texto: ")
contarTXT(archivo,palabra)


#cont=contando(texto,palabra)
#print("La palabra: ",palabra,"aparece: ",cont,"veces en este texto")



