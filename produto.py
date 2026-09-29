print("CADASTRO DE PRODUTO")

nome = input("Produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))

print()
print("Produto cadastrado com sucesso!")
print()
print("Produto:", nome)
print(f"Preço: R$ {preco:.2f}")
print("Quantidade:", quantidade)