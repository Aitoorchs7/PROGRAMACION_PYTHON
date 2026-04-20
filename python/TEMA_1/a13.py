nota1 = float(input("Nota del primer trimestre:"))
nota2 = float(input("Nota del segundo trimestre:"))
nota3 = float(input("Nota del tercer trimestre:"))


expediente = (nota1 + nota2 + nota3)/3
boletin = int(expediente)

print("LA nota del boletin es",boletin,"mientras que la del expediente es",expediente)