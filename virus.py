print('Insira apenas números entre 0 a 99')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite outro número: '))

if a < 0 or a > 99 or b < 0 or b > 99:
    print('Por favor, apenas números inteiros de 0 a 99')

#desmembrando o numero solicitado
caracter1 = a // 10    
caracter2 = a % 10

#eliminando o numero 7 e trocando por 0
if caracter1 == 7:
    caracter1 = 0
else: caracter1 = caracter1
    
if caracter2 == 7:
    caracter2 = 0
else: caracter2 = caracter2

#voltando os caracteres 
caracter1 = caracter1 *10

numero1 = caracter1 + caracter2

#desmembrando o outro numero solicitado
caracter3 = b // 10
caracter4 = b % 10  

#eliminando o numero 7 e trocando por 0
if caracter3 == 7:
    caracter3 = 0
else:caracter3 = caracter3
    
if caracter4 == 7:
    caracter4 = 0
else:caracter4 = caracter4
    
#voltando os caracteres   
caracter3 = caracter3 * 10

numero2 = caracter3 + caracter4

#fazendo a soma
soma = numero1 + numero2

#desmembrando a soma
num1 = soma // 100
resto = soma % 100
num2 = resto // 10
num3 = resto % 10

#eliminando os 7 da soma
if num1 == 7:
    num1 = 0
else: num1 = num1


if num2 == 7:
    num2 = 0 
else: num2 = num2

if num3 == 7:
    num3 = 0
else: num3 = num3

#voltando os caracteres
result1 = num1 * 100
result2 = num2 * 10

#resultado final
final = result1 + result2 + num3



print(f'a soma dos numeros é: {final}')