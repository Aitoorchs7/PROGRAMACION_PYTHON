hora, minuto, segundo = map(int, input("Introduce la hora actual separando por(:):  ").split(':'))

segundo += 1

match segundo:
    case segundo if 0 < segundo <= 59:
        print(hora,":",minuto,":",segundo)
    case 60 if minuto == 59:
        minuto = 0
        segundo = 0
        hora = hora + 1
        print(hora,":",minuto,":",segundo)
    case 60 if minuto < 59:
        segundo = 0
        minuto = minuto + 1
        print(hora,":",minuto,":",segundo)
    case segundo if segundo < 0:
        print("Introduce una hora dentro de los limites")
    case segundo if segundo > 60:
        resto = segundo - 60
        segundo = resto
        minuto = minuto + 1
        print(hora,":",minuto,":",segundo)
    case _: 
        print("Hora incorrecta")
        