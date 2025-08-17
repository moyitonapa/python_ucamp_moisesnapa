# Programa que calcula el promedio de un alumno
# Se pide el nombre, la edad y 8 notas de las materias del alumno
# Se calcula el promedio de las notas y se imprime el promedio final

nombre = input('Nombre del alumno: ')
print('Hola ' + nombre)

# se solicitan las notas de las materias del alumno
a = float(input('Matématicas: '))
b = float(input('Español: '))
c = float(input('Historia: '))
d = float(input('Ciencias: '))
e = float(input('Biología: '))
f = float(input('Física: '))
g = float(input('Geografía: '))
h = float(input('Arte: '))

# se calcula el promedio de las notas
promedio = (a + b + c + d + e + f + g + h) / 8

print(f'{nombre }Tú promedio general es de: {promedio}')
if promedio >= 9.0:
    print('¡Felicidades! ¡Has superado el promedio!')
elif promedio >= 7.0:
    print('¡Buenas noticias! ¡Has superado el promedio!')
elif promedio >= 6.0:
    print('¡Apenas superaste el promedio!')
else:       
    print('¡REPROBADO!')
