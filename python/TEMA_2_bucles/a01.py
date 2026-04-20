num = int
print("Introduce numeros enteros(0 para terminar)")
while True:
    num = int(input())
    if num == 0:
        break
    # para hacer un do while y que se ejecute el codigo una vez obligatoriamente
    # pondremos una condiion siempre cierta y otra para que salga del bucle
 
    print("Este numero es par") if num % 2 == 0 else print("Este numero es inpar")

    print("Es positivo ") if num > 0 else print ("Es negativo ")

    print("El cuadrado de este numero es",num*num)
print("Fin del programa")
#todo lo que no este tabulado uno a la derecha, no este dentro del bucle
#por lo que se cierra pasando de linea a la izquierda
