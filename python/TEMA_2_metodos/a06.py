n = int(input("Introduce un numero: "))

class numerosPares():
    def pares(self, n):
        for i in range (0,n + n,2):
            print(i)

objeto = numerosPares()
objeto.pares(n)