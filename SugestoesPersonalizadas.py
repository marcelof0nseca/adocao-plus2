from CrudAnimais import AMARELO, RESET



def sugestoes_personalizadas(idade, especie):

    adotantes = []
    cuidados = []
    compatibilidade = []
    atividades = []

    if especie == "cachorro":
        if idade <= 1:
            adotantes = ["Famílias com crianças", "Adultos ativos"]
            cuidados = ["Vacinação em dia", "Treinamento inicial"]
            compatibilidade = ["Sociável com outros cães"]
            atividades = ["Brincadeiras curtas", "Passeios leves"]
        elif idade <= 3:
            adotantes = ["Adultos jovens", "Famílias"]
            cuidados = ["Exercícios regulares", "Alimentação balanceada"]
            compatibilidade = ["Pode conviver com gatos se socializado"]
            atividades = ["Passeios longos", "Treinamento avançado"]
        elif idade <= 6:
            adotantes = ["Adultos", "Famílias ativas"]
            cuidados = ["Exames veterinários periódicos", "Controle de peso"]
            compatibilidade = ["Compatível com cães e gatos dependendo da socialização"]
            atividades = ["Agility", "Jogos interativos"]
        elif idade <= 10:
            adotantes = ["Adultos tranquilos", "Famílias"]
            cuidados = ["Check-ups frequentes", "Alimentação especial"]
            compatibilidade = ["Prefere ambientes calmos"]
            atividades = ["Caminhadas moderadas", "Companhia constante"]
        else:
            adotantes = ["Pessoas idosas", "Adultos tranquilos"]
            cuidados = ["Atenção à saúde", "Alimentação para cães idosos"]
            compatibilidade = ["Melhor em lares com poucos animais"]
            atividades = ["Caminhadas leves", "Descanso confortável"]

    elif especie == "gato":
        if idade <= 1:
            adotantes = ["Famílias com crianças", "Adultos jovens"]
            cuidados = ["Vacinação em dia", "Brinquedos para gastar energia"]
            compatibilidade = ["Sociável com outros gatos"]
            atividades = ["Brincadeiras interativas", "Arranhadores"]
        elif idade <= 4:
            adotantes = ["Adultos jovens", "Famílias"]
            cuidados = ["Alimentação balanceada", "Ambiente enriquecido"]
            compatibilidade = ["Pode conviver com cães se acostumado"]
            atividades = ["Exploração de prateleiras", "Brincadeiras moderadas"]
        elif idade <= 8:
            adotantes = ["Adultos", "Famílias tranquilas"]
            cuidados = ["Exames veterinários periódicos", "Controle de peso"]
            compatibilidade = ["Compatível com gatos calmos"]
            atividades = ["Sessões de carinho", "Brincadeiras leves"]
        elif idade <= 12:
            adotantes = ["Adultos tranquilos", "Pessoas idosas"]
            cuidados = ["Check-ups frequentes", "Alimentação especial"]
            compatibilidade = ["Prefere ambientes calmos"]
            atividades = ["Companhia tranquila", "Descanso confortável"]
        else:
            adotantes = ["Pessoas idosas", "Adultos tranquilos"]
            cuidados = ["Atenção à saúde", "Alimentação para gatos idosos"]
            compatibilidade = ["Melhor em lares com poucos animais"]
            atividades = ["Descanso", "Companhia constante"]

    else:
        print("Espécie inválida. Use 'gato' ou 'cachorro'.")
        return

    print(f"\n{AMARELO}SUGESTÕES PERSONALIZADAS:{RESET}")
    print("Adotantes:", ", ".join(adotantes))
    print("Cuidados:", ", ".join(cuidados))
    print("Compatibilidade:", ", ".join(compatibilidade))
    print("Atividades:", ", ".join(atividades))


def main_sugestoes():
    print("=== Sistema de Sugestões Personalizadas ===")
    idade = int(input("Digite a idade do animal: "))
    especie = input("Digite a espécie (gato/cachorro): ").lower()
    sugestoes_personalizadas(idade, especie)

if __name__ == "__main__":
    main_sugestoes()  # Só roda se você ABRIR esse arquivo diretamente
