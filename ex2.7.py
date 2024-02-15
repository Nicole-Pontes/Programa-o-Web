texto = "12345"
numero = "1234567890"
e_inteiro = True
for caractere in texto:
    if caractere not in numero:
        e_inteiro = False
        break
if e_inteiro:
    print("É um número inteiro!")
else:
    print ("Não é um número inteiro!")