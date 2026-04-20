num1 = int(input("Introduce un numero: "))
num2 = num1 + 1
factorial = 0
suma = 1

print("El factorial de",num1,"es: ")
for i in range(num1 - 1,-1,-1):

    if i != 0:
        num1 *= i
    else:
        break

    
print(num1)