#ejemplos para entradas de usuarios 


import random # se importo la biblioteca que hace posible generar un comportamiento aleatoreo 

print("Vamos a comenzar con la practica para ingresar datos en una consola")

nombre= input("Ingresa tu nombre porfavor: ")
edad= int(input("Tu edad tambien: "))

print("Hola", nombre, "nos dijiste que tienes ",edad, "años")
if edad >= 18:
        print("Acceso consedido")
        apuesta = int(input("Ingresa tu apuesta: "))
        print("¡VAMOS A JUAGAR!\n")
        print("GANALE A LA MAQUINA")
        numero = random.randint(1, 100)  # Genera un número entero entre 1 y 100
        if apuesta >= numero:
                print("Tu apuesta fue: ", apuesta)
                print("La maquina aposto: ",numero)
                print("FELICIDADES, GANASTE")
        else:
                print("Tu apuesta fue: ", apuesta)
                print("La maquina aposto: ",numero)
                print("TE GANO LA MAQUINA")

else:
        print("Acceso denegado")
        print("Ya no podemos continuar. ¡LO SENTIMOS!")

