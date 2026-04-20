letra = input("Introduce una letra: ")

class esVocal():
    def vocal(self,letra):
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'á' or letra == 'é' or letra == 'í' or letra == 'ó' or letra == 'ú' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            return True
        else:
            return False

objeto = esVocal()
vocal = objeto.vocal(letra)
print("Esta letra es vocal?",vocal)