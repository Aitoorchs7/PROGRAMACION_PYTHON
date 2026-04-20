num = 7

# ponemos un numero alto en el for para asegurar que llega a 100
for i in range(20):
    resultado = num * i

    if resultado >= 100:
        break
    # para poner un limite, ponemos un break en la condicion que haga que salga
    print(num,"*",i,"=",resultado)