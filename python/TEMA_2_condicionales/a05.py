numero1, numero2 = map(int, input("Introdce dos numeros:").split())

if numero1 > numero2:
    print(numero1,"es mayor que",numero2)
elif numero1 < numero2:
    print(numero2,"es mayor que",numero1)
else:
    print(numero1,"es igual que",numero2)

