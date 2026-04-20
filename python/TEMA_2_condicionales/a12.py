dia, mes, año = map(int, input("Introduce la fecha de hoy: ").split('/'))

dia += 1

match dia:
    case dia if mes == 2 and dia >= 29: 
        resto = dia - 29
        dia = resto
        mes = 3
        dia = dia + 1 if dia == 0 else dia
        print(dia,mes,año)
    case dia if mes == 4 | mes == 6 | mes == 9 | mes == 11 and dia > 30:
        resto = dia - 30
        dia = resto
        mes += 1
        print(dia,mes,año)
    case dia if mes == 1 | mes == 3 | mes == 5 | mes == 7 | mes == 8 | mes == 10 | mes == 12 and dia > 31:
        resto = dia - 31
        dia = resto
        mes = 1, año + 1 if mes == 12 else mes + 1
        print(dia,mes,año)
    case dia if 0 < dia <= 30:
        print(dia,mes,año)
    case dia if dia <= 0:
        print("Fecha incorrecta")
    case _:
        print("Fecha incorrecta")

        