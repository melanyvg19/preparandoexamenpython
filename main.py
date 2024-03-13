bandas=[]
banda={}

#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("*" * 20) 

opcion=100

while(opcion != 5):

    print("1. Registrar banda")
    print("2. Buscar información de una banda")
    print("3. Mostrar agenda del evento")
    print("4. Modificar una banda")
    print("5. Salir")

    opcion= int(input("Digita una opción"))
    if opcion == 1:
        banda={}
        ## Crear datos del diccinario
        banda["id"]=int(input("Digite el id  "))
        banda["nombre"]= input("Nombre de la banda  ")
        banda["genero"]= input("Digite el genero de la banda  ")
        banda["clasificacion"] = input("Clasificación:  ")
        banda["tiempo"]= int(input("Tiempo:   "))
        banda["costo"]= int(input("Costo:  $"))
        
        #Agregar el diccionario a la lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada=input("Nombre de la banda que estás buscando")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]== bandaBuscada:
                #Mostrar los datos ede bandAuxiliar
                print(f"id: {bandAuxiliar["id"]} --- Nombre:  {bandAuxiliar["nombre"]}")

            else:
                print("No lo encontré")

    elif opcion == 3:
        print(bandas)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass