seg, min, h = map(int, input("Escribe la hora que desee convertir a segundos con : :").split(':'))
todo = 0

class todoSegundos():
    def segundos(self, seg, min, h):
        min = 60* min
        h = 3600* h

        todo = seg + min + h
        return todo

objeto = todoSegundos()
todo = objeto.segundos(seg,min,h)
print("Todo en segundos es:",todo)
