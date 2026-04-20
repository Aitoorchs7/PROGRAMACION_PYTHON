nota = int(input("Intoduzca tu nota: "))

match nota: 
    case nota if 0 <= nota <=4:
        print("Suspenso")
    case nota if 4 < nota <= 5:
        print("Suficiente")
    case nota if 5 < nota <= 6:
        print("Bien")
    case nota if 6 < nota <= 8:
        print("Notable")
    case nota if 8 < nota <= 10:
        print("Sobresaliente")
    case _:
        print("La nota debe estar comprendida entre 0 y 10")
    #el case_ es como en el caso de que no sea ninguna de los casos