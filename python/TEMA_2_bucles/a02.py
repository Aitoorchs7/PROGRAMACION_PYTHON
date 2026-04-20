edad = int
suma = 0
media = 0
total = 0
mayor = 0
print("Introduce las edades de los alumnos, escribe un numero negativo para terminar")

while True:
    edad = int(input("Edad: "))

    if edad > 0:
        suma += edad
        total += 1
        media = (suma/total)
        if edad >= 18:
            mayor += 1
    elif edad < 0:
        break

print("El total de alumnos son:",total)
print("Que entre todos suman",suma)
print("Su media de edad es de",media,"años")
print("Y",mayor,"alumnos son mayores de edad")

