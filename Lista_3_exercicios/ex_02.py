# Lista usando laço for
print(" ")
print("Lista de Lojas")
print(" ")

lojas = ["Minas Gerais", "São Paulo", "Espírito Santo", "Rio de Janeiro"]

# Listar usando laço com índice
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")
    print(" ")