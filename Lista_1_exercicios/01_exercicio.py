# Variáveis
nome = "Isabelle"
idade = 17
altura = 1,59
peso = 59
cidade = "Morumbi"

# Exibição de valores
print (nome)
print (idade)
print (altura)
print (peso)
print (cidade)
print ("\n")

# # 1º método de concatenação (string: str)
# print("O meu nome é: " + nome + " e tenho " + str(idade) + " anos.\n")

# 2º método de concatenação (format)
print("O meu nome é {} e tenho {} anos. Minha altura é {} o meu peso {} e moro na cidade {} \n" .format(nome, idade, altura, peso, cidade))

# # 3º método de concatenação (f string)
# print(f"O meu nome é: {nome} e tenho {idade} anos.\n")