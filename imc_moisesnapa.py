#Código que calcula el Indice de Maza Corporal (IMC)
#---------Moisés Nápoles Pacheco---------#

print('¡Conoce tú estado de nutrición!')  
print('Vámos a calcular tu IMC\n')
nombre = input('Para iniciar es necesario que nos proporiones tu nombre completo: ') # le pedimos el nombre
edad = int(input('¿Cuántos años tienes?')) # le pedimos la edad
peso = float(input('¿Cuánto pesas en kilogramos?')) # le pedimos la masa
altura = float(input('¿Cuánto mides en metros?\n')) # le pedimos la altura
print(f'Nombre: {nombre}\nEdad: {edad}\nPeso: {peso}\nAltura: {altura}') # imprimimos la informacion
imc = peso / (altura ** 2) # calculamos el IMC
print(f'{nombre} tú IMC es de: {round(imc, 2)}') # imprimimos el IMC