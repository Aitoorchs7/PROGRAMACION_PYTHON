altura = 0
mayor = 0 
contador1 = 0
contador2 = 0

print("Para comenzar el programa de los arboles introduce la altura del primero")
print ("Para terminar el programa introduce -1")

while altura != -1:
    altura = int(input())
    contador1 += 1 

    if mayor < altura:
        mayor = altura 
        contador2 = contador1 - 1

print("El arbol mas alto es",mayor)
print("Y su numero de etiqueta es",contador2)    
