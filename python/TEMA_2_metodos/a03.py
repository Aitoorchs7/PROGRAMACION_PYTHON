opcion = int(input("Para calcular el area pulse 1, para calcular el volumen pulse 2: "))

radio, altura = map(float, input("Introduzca el radio y la altura del cilindro: ").split())

PI = 3.1415

class Calculos():
    def resultado(self, radio, altura, PI, opcion):
        if opcion == 1:
            resultado = 2*PI * radio*(altura + radio)
            print("El area del cilindro es de",resultado,"unidades")
        elif opcion == 2:
            resultado = PI * (radio*radio) * altura
            print("El volumen del cilindro es de",resultado,"unidades")
        else:
            print("Opcion no valida")

objeto = Calculos()
objeto.resultado(radio, altura, PI, opcion)



