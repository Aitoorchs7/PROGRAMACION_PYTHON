import random

resultado = 0
racha = 0
print("Bienvenido al juego del calculo mental, comencemos:")

while True:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    print(num1,"+",num2)
    resultado = int(input("Resultado: "))
    if resultado != (num1 + num2):
        print("Solucion incorrecta")
        print("La solucion era:",num1 + num2)
        break
    else:
        racha += 1

              