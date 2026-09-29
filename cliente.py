print("================================")
print("     CADASTRO DE CLIENTE")
print("================================")

# Nome
nome = input("Nome do cliente: ")

# E-mail
while True:
    email = input("E-mail: ")

    if email.endswith("@gmail.com") or email.endswith("@hotmail.com"):
        break
    else:
        print("E-mail inválido! Digite corretamente usando @gmail.com ou @hotmail.com.")

# Telefone
while True:
    telefone = input("Telefone: ")

    # Verifica se todos os caracteres são números
    if not telefone.isdigit():
        print("Telefone inválido! Digite apenas números.")
    
    # Verifica se possui 10 ou 11 números
    elif len(telefone) > 11:
        print("Quantidade de números inválida! O telefone deve ter no máximo 11 números.")
    
    elif len(telefone) < 10:
        print("Quantidade de números inválida! O telefone deve ter 10 ou 11 números.")
    
    else:
        break

# Exibição dos dados
print()
print("================================")
print("Cliente cadastrado com sucesso!")
print("================================")
print("Nome:", nome)
print("E-mail:", email)
print("Telefone:", telefone)