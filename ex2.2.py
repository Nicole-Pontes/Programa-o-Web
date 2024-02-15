nu1 = int(input("Digite um número: "))

if (nu1<0):
    status = "negativo"
elif (nu1>0):
    status = "positivo"
else:
    status = "zero"

print (f"O número é {status}")