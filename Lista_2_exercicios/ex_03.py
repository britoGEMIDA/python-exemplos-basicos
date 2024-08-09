# 
print("==-LOGIN-==")

# Input
nome = input("Insira o nome de usuário: ")
senha = input("Insira a senha: ")

# verificação do login e senha
if nome == 'admin' and senha == '1234':
    print("Sucesso!")
else:
    print("Erro.")