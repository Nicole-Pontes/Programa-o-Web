import math

a = int(input("Escreva o valor de a: "))
b = int(input("Escreva o valor de b: "))
c = int(input("Escreva o valor de c: "))

delta = b ** 2 - 4 * a * c

if (delta == 0):
    raiz = (-b + math.isqrt(delta)) / 2 * a
    print(f"O resultado é {raiz}")
elif (delta < 0):
    print ("A raiz não é um número real")
else:
    raiz = (-b + math.isqrt(delta)) / 2 * a
    raiz2 = (-b - math.isqrt(delta)) / 2 * a
    print(f"As raízes são {raiz} {raiz2}")