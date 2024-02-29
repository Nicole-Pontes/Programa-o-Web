numeros = "1234567890.,"
texto = input("Escreva algo: ")

for caractere in texto:
    if caractere in numeros:
        inteiro = True
    else:
        inteiro = False
        break
if inteiro:
    print ("É um número")
else:
    print ("Não é um número")