#antes hay que importar random como en java
import random

numeroSecreto = random.randint(1,100)
# en python, para generar un numero aleatorio
# solamente con poner que el numero = random.random("Intervalo")
# se genera automaticamente, ademas con randint se genera un numero entero
eleccion = 0
print("Bienvenido al juego de la numero secreta")
print("Ve introduciendo numeros, si te rindes introduce -1")

while True:
    eleccion = int(input("Introduce el numero: "))

    if eleccion > 0:
        if eleccion > numeroSecreto:
            print("El numero secreto es menor al introducido")
        elif eleccion < numeroSecreto:
            print("El numero secreto es mayor al introducido")
        elif eleccion == numeroSecreto:
            print("Felicidades has ganado, el numero secreto era",numeroSecreto)
            break
    else:
        print("Ups... La proxima vez será")
        break
   

        