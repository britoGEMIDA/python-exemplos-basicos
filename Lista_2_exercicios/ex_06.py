comida = int(input("Indique o alimento: "))

# Função para selecionar sabor
def alimento(comida):
    match comida:
        case 1:
            print("Pizza.")
        case 2:
            print("Hamburguer.")
        case 3:
            print("Salada.")
        case _:
            print("Sabor inválido!")

alimento(comida)