num1, num2 = map(int, input("Introduce dos numeros: ").split())

class Comprendidos():
    def mensaje(self,num1, num2):
        print("Los numeros comprendidos entre",num1,"y",num2,"es: ")

    def numeros(self, num1, num2):
        if num1 > num2:
            for i in range(num2, num1 + 1):
                print(i)
        else:
            for i in range(num1, num2 + 1):
                print(i)

objeto = Comprendidos()
objeto.mensaje(num1, num2)
objeto.numeros(num1,num2)            