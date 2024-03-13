tipo = input("Escreva qual tipo de triângulo é (isósceles, equilátero ou escaleno): ")
altura = float(input("Escreva a altura desse triângulo: "))
largura = float(input("Escreva o cumprimento da base (caso seja um triângulo isósceles escreva o tamanho do lado que difere dos outros dois): "))

area = (largura * altura)/2

if (tipo == "isósceles"):
    lado = ((largura/2) ** 2 + altura ** 2) ** 0.5
    perimetro = lado * 2 + largura
elif (tipo == "escaleno"):
    lado = float(input("Escreva o tamanho do segundo lado (já que o primeiro é o comprimento da base): "))
    lado_2 = float (input("Escreva o tamanho do segundo lado: "))
    perimetro = largura + lado + lado_2
else:
    perimetro = largura * 3

print(f"A área desse triângulo é igual a {area} e o perímetro é igual a {perimetro}")