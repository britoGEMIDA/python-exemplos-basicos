dia = input("Indique o dia da semana: ")

# Função Fim de Semana
def dia_da_semana(dia):
    match dia:
        case "Domingo" | "Sábado":
            return "Fim de semana"
        case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
            return "Dia útil"
        case _:
            return "Valor inválido!"
        
print(dia_da_semana(dia))