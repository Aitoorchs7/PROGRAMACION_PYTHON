num1, num2 = map(int,input("Introduce dos numeros: ").split())
mayor = 0

class Mayores():
    def mayor(self,num1,num2):
        if num1 == num2:
            print("Estos numeros son iguales: ")
        else:
            mayor = num1 if num1 > num2 else num2
            return mayor
        
objeto = Mayores()

# se puede hacer de dos maneras, print(objeto.mayor(num1,num2)) si no voy a ultilizar el resultado
#o si si seria de esta manera:

mayor = objeto.mayor(num1,num2)
print("El mayor de los dos es",mayor)