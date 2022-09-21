#Ejesicio 1------------------------------------------------------------------------------------------------------------------

def operaciones_matematicas(num1, num2):
    if num1.isdigit() and num2.isdigit():
        suma = (int(num1) + int(num2))
        resta = (int(num1) - int(num2))
        producto = (int(num1) * int(num2))
        division = (float(num1) / float(num2))
        print('La suma de ambos numeros es: ', (suma))
        print('La resta entre ambos numeros es: ', (resta))
        print('El producto de ambos numeros es: ', (producto))
        print('La division de ambos numeros es: ', (division))
    else:
        print('Alguno de los valores ingresados, no es un numero.')

num1 = input('Ingresa el valor numerico 1: ')
num2 = input('Ingresa el valor numerico 2: ')

operaciones_matematicas(num1, num2)

#Ejersicio 2----------------------------------------------------------------------------------------------------------------

def mayor(nums):
    x = 0
    for num in nums:
        if num > x:
            x = num
    print('El numero mayor es: ', (x))

nums = []

for i in range(3):
    num = input('Ingresa el valor numerico ' + str(i+1) +': ')
    if num.isdigit():
        num = int(num)
        nums.append(num)

mayor(nums)

#Ejersicio 3-----------------------------------------------------------------------------------------------------------------

def descuento():
    while True:
        importe = input('Ingresa el monto del producto a comprar: ')
        if importe.isdigit():
            importe = int(importe)
            break
    desc = (importe / 100) * 15
    importe_final = importe - desc
    print('Importe produto: ', (importe))
    print('Descuento producto: ', (desc))
    print('Importe final: ', (importe_final))

descuento()

#Ejersicio 4-----------------------------------------------------------------------------------------------------------------
def evalua_notas(nota):
    if nota in range(1, 3):
        print('Ha desaprobado')
    elif nota in range(4,6):
        print('Ha obtenido un aprovado')
    elif nota in range(7, 8):
        print('Ha obtenido una calificacion notable')
    else:
        print('Ha obtenido una calificacion sobresaliente')


while True:
    nota = input('Ingresa nota: ')
    if nota.isdigit(): 
        nota = int(nota)
        if nota in range(1,11):
            evalua_notas(nota)
            break
        else:
            print('Nota fuera de rango')

#Ejersicio 5-----------------------------------------------------------------------------------------------------------------
def hola():
    for i in range(5):
        print('Hola')
hola()

#Ejersicio 6-----------------------------------------------------------------------------------------------------------------
def pares(entero):
    for i in range(entero):
        if i % 2 == 0:
            print(i)

while True:
    entero = input('Ingresa un valor numerico positivo: ')
    if entero.isdigit():
        entero = int(entero)
        pares(entero)
        break