PRECIOM = 2.35
PRECIOP = 1.95

pesoManzanas1 = int(input("Introduce los kilos de manzanas del primer semestre: ")) 
pesoPeras1 = int(input("Ahora el de peras del primer trimestre: "))
pesoManzanas2 = int(input("Ahora las manzanas del segundo semestre: "))
pesoPeras2 = int(input("Y por ultimo los kilos de peras del segundo trimestre: "))

precioTotalM = ((pesoManzanas1 + pesoManzanas2) * PRECIOM)
precioTotalP = ((pesoPeras1 + pesoPeras2)* PRECIOP)
precioTotal = precioTotalM + precioTotalP
print("El importe total anual es de:",precioTotal,"euros")