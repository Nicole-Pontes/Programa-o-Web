produto = input("Escreva o nome do produto: ")
preco_compra = float(input("Escreva o valor que foi pago: "))
preco_venda = float(input("Escreva o valor que será vendido: "))
estoque = int(input("Escreva a quantidade que tem no estoque: "))

lucro = (preco_venda * estoque) - (preco_compra * estoque)

print(f"O lucro previsto se for vendido todo o estoque de {produto} é de {lucro}")