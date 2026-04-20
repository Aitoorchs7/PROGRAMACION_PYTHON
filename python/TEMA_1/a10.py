llueve = input("Esta lloviendo: ") == True
tareas = input("Has terminado las tareas: ") == True
biblioteca = input("Necesitas ir a la biblioteca: ") == True

salir = (tareas and not llueve) or biblioteca

print("Puedes salir a la calle:",salir) 


