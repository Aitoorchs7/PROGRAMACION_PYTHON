
num = int(input("Introduce un numero complendido entre 1 y 10: "))

if 0 < num <= 10:
    for i in range(11):
        resultado = num * i
        print(num,"*",i,"=",resultado)
else:
    print("Numero introducido incorrecto")