letra = (input("Digite uma letra: "))

if (letra in {"a", "e", "i", "o", "u"}):
    print("Essa letra é uma vogal.")
elif (letra in {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "y", "z"}):
    print ("Essa letra é uma consoante.")
else:
    print ("Não é uma letra que faz parte do alfabeto latino")