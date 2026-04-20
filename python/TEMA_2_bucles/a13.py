n = int(input("Introduce un número: "))

# Bucle externo: controla cuántas filas vamos a hacer (de n hasta 1)
for i in range(n, 0, -1):
    
    # Bucle interno: dibuja los asteriscos de UNA fila
    for j in range(i):
        print("*", end=" ")  # Pinta y se queda en la misma línea
        # end = y lo que sea hace que se evide el salto de linea 
        
    print()  # Al terminar el bucle interno, hacemos un salto de línea vacío para la siguiente fila
