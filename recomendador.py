# Recomendador
from CrudAnimais import carregar_animais, AMARELO, RESET

def recomendar_animal():
    """
    Recomenda um animal baseado no perfil do adotante.
    Pergunta características e escolhe o mais compatível.
    """

    print("\n=== RECOMENDAÇÃO DE ANIMAL ===")

    especie_p = input("Qual espécie você prefere? (cachorro/gato/outro): ").strip().lower()
    temperamento_p = input("Prefere comportamento calmo, ativo ou indiferente? ").strip().lower()
    idade_p = input("Prefere filhote, jovem, adulto, idoso ou indiferente? ").strip().lower()

    animais = carregar_animais()

    if not animais:
        print("\nNenhum animal cadastrado para recomendar.")
        return

    melhor_animal = None
    melhor_pontuacao = -1

    for a in animais:
        pontuacao = 0

        # Preferência de espécie
        if especie_p != "indiferente" and especie_p == a["especie"].lower():
            pontuacao += 2

        # Temperamento (busca palavras no comportamento)
        if temperamento_p != "indiferente" and temperamento_p in a["comportamento"].lower():
            pontuacao += 2

        # Idade (avaliando texto)
        if idade_p != "indiferente" and idade_p in a["idade"].lower():
            pontuacao += 1

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_animal = a

    if melhor_animal is None or melhor_pontuacao == 0:
        print("\nNenhum animal combina claramente com o perfil informado.")
        return

    print(f"\n{AMARELO}=== ANIMAL RECOMENDADO ==={RESET}")
    print(
        f"ID: {melhor_animal['id']}\n"
        f"Nome: {melhor_animal['nome']}\n"
        f"Espécie: {melhor_animal['especie']}\n"
        f"Raça: {melhor_animal['raca']}\n"
        f"Idade: {melhor_animal['idade']}\n"
        f"Sexo: {melhor_animal['sexo']}\n"
        f"Estado de saúde: {melhor_animal['estado_saude']}\n"
        f"Data de chegada: {melhor_animal['data_chegada']}\n"
        f"Comportamento: {melhor_animal['comportamento']}"
    )
