numero = int(input("Introduzca un numero: "))

numero = -numero if numero < 0 else numero #es necesario asignar el nuevo valor de numero.

if numero >= 0 and numero < 10:
    print("El numero",numero,"tiene una cifra")
elif numero >= 10 and numero < 100:
    print("El numero",numero,"tiene dos cifras")
elif numero >= 100 and numero < 1000:
    print("El numero",numero,"tiene tres cifras")
elif numero >= 1000 and numero < 10000:
    print("El numero",numero,"tiene cuatro cifras")
elif numero >= 10000 and numero < 100000:
    print("El numero",numero,"tiene cinco cifras")
elif numero > 100000:
    print("El numero",numero,"es mayor a los numeros comprendidos")

    #python permite encadenar condiciones, por lo que seria mas limpio por ejemplo: 
    # 0 <= numero < 10 y asi con todos.
    #tambien existe un metodo para coNvertir valor absoluto que es abs(numero)

