#Código que calcula el Índice de Maza Corporal (IMC)
#---------Moisés Nápoles Pacheco---------#

print('¡Conoce tú estado de nutrición!')  
print('Vámos a calcular tu IMC\n')
nombre = input('Para iniciar es necesario que nos proporiones tu nombre completo: ') # le pedimos el nombre
while True:     
            try: 
                edad = int(input('¿Cuántos años tienes?')) # le pedimos la edad
                break
            except ValueError:
                print('¡No es un numero entero! Por favor ingrese un numero entero')
while True:
            try:
                peso = float(input('¿Cuánto pesas en kilogramos?')) # le pedimos la masa
                break
            except ValueError:
                print('¡NO ES UN NUMERO FLOTANTE! Vuelve a intentarlo.')
while True:
            try:
                altura = float(input('¿Cuánto mides en metros?')) # le pedimos la altura
                break
            except ValueError:
                print('¡No es un numero flotante! Por favor ingrese un numero flotante')

print(f'\nNombre: {nombre}\nEdad: {edad}\nPeso: {peso}\nAltura: {altura}') # imprimimos la informacion
imc = peso / (altura ** 2) # calculamos el IMC
print(f'\n{nombre} tú IMC es de: {round(imc, 2)}') # imprimimos el IMC

if imc<15.00:
    print('Tienes Delgadez severa')
elif imc>=15.00 and imc<=16.99:
            print('Tienes Delgadez moderada')
elif imc>=17.00 and imc<=18.49:
            print('Tienes Delgadez leve')
elif imc>=18.50 and imc<=24.99:
            print('Estas en tu peso ideal')
elif imc>=25.00 and imc<=29.99:
            print('Tienes Sobrepeso')
else: 
            print('Tienes Obesidad morbida')