dia, mes, año = map(int, input("Introduce una fecha en el orden dia/mes/año: ").split('/'))
#split('') recoge los datos separandolos dependiendo lo que pongamos dentro

if 0 < año <= 2025:
    match mes: 
        case 2: 
            print("Fecha correcta") if 0 < dia <= 28 else print("Fecha incorrecta")
        case 4 | 6 | 9 | 11: 
            print("Fecha correcta") if 0 < dia <= 30 else print("Fecha incorrecta")
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print("Fecha correcta") if 0 < dia <= 31 else print("Fecha incorrecta")
        case _:
            print("Fecha incorrecta")
else: 
    print("Fecha incorrecta")

# en python, los casos se separan con una varra vertical (caso1|caso2)