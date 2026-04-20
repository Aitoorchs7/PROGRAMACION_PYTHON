num = int(input("Introduce un numero: "))

class Eco():
    def rep(self, veces):
        for i in range (veces):
            print("eco...")

# 2. Instancias la clase (creas el objeto)
mi_objeto = Eco()
# 3. Llamas al método desde el objeto y le pasas el número
mi_objeto.rep(num)
# num se va a convertir en veces cuando entre al metodo

