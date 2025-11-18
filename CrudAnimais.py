# CrudAnimais.py
ARQUIVO_ANIMAIS = "animais.txt"

# Cores (ANSI)
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'


def carregar_animais():
    """
    Lê animais no formato:
    id;nome;especie;raca;idade;sexo;estado_saude;data_chegada;comportamento
    Retorna lista de dicts.
    """
    animais = []
    try:
        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                if len(partes) < 9:
                    # linha incompleta -> ignora
                    continue
                try:
                    animais.append({
                        "id": int(partes[0]),
                        "nome": partes[1],
                        "especie": partes[2],
                        "raca": partes[3],
                        "idade": partes[4],
                        "sexo": partes[5],
                        "estado_saude": partes[6],
                        "data_chegada": partes[7],
                        "comportamento": partes[8]
                    })
                except:
                    continue
    except FileNotFoundError:
        pass
    return animais


def salvar_animais(animais):
    """Escreve lista de animais no arquivo (substitui tudo)."""
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arq:
        for a in animais:
            arq.write(
                f"{a['id']};{a['nome']};{a['especie']};{a['raca']};"
                f"{a['idade']};{a['sexo']};{a['estado_saude']};"
                f"{a['data_chegada']};{a['comportamento']}\n"
            )


def _proximo_id(animais):
    """Retorna próximo ID baseado na lista (auto-increment)."""
    if not animais:
        return 1
    try:
        max_id = max(a["id"] for a in animais)
        return max_id + 1
    except:
        return len(animais) + 1


def id_existe_animal(id_animal):
    """Verifica se um ID de animal existe (True/False)."""
    animais = carregar_animais()
    for a in animais:
        if a["id"] == id_animal:
            return True
    return False


def adicionar_animal():
    """Adiciona novo animal (ID gerado automaticamente)."""
    animais = carregar_animais()
    novo_id = _proximo_id(animais)

    print(f"ID gerado: {novo_id} (não é necessário digitar)")

    nome = input("Nome: ").strip()
    especie = input("Espécie: ").strip()
    raca = input("Raça: ").strip()
    idade = input("Idade: ").strip()
    sexo = input("Sexo: ").strip()
    estado_saude = input("Estado de saúde: ").strip()
    data_chegada = input("Data de chegada (DD/MM/AAAA): ").strip()
    comportamento = input("Comportamento: ").strip()

    animais.append({
        "id": novo_id,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "sexo": sexo,
        "estado_saude": estado_saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento
    })

    salvar_animais(animais)
    print(VERDE + f"Animal cadastrado com sucesso! (ID: {novo_id})" + RESET)


def visualizar_animais():
    """Mostra a lista de animais formatada."""
    animais = carregar_animais()
    if not animais:
        print(VERMELHO + "Nenhum animal cadastrado." + RESET)
        return

    print(AZUL + "\n=== ANIMAIS CADASTRADOS ===" + RESET)
    for a in animais:
        print(
            f"ID: {a['id']} | Nome: {a['nome']} | Espécie: {a['especie']} | Raça: {a['raca']} | "
            f"Idade: {a['idade']} | Sexo: {a['sexo']} | Estado: {a['estado_saude']} | "
            f"Chegada: {a['data_chegada']} | Comportamento: {a['comportamento']}"
        )


def editar_animais():
    """Editar animal por ID (mantém campos se entrada vazia)."""
    animais = carregar_animais()
    if not animais:
        print(VERMELHO + "Nenhum animal cadastrado." + RESET)
        return

    visualizar_animais()
    try:
        id_edit = int(input("ID do animal a editar: ").strip())
    except:
        print(VERMELHO + "ID inválido!" + RESET)
        return

    for a in animais:
        if a["id"] == id_edit:
            print("Deixe vazio para manter o valor atual.")
            novo_nome = input(f"Nome [{a['nome']}]: ").strip()
            novo_especie = input(f"Espécie [{a['especie']}]: ").strip()
            nova_raca = input(f"Raça [{a['raca']}]: ").strip()
            nova_idade = input(f"Idade [{a['idade']}]: ").strip()
            novo_sexo = input(f"Sexo [{a['sexo']}]: ").strip()
            novo_estado = input(f"Estado de saúde [{a['estado_saude']}]: ").strip()
            nova_data = input(f"Data de chegada [{a['data_chegada']}]: ").strip()
            novo_comport = input(f"Comportamento [{a['comportamento']}]: ").strip()

            if novo_nome:
                a["nome"] = novo_nome
            if novo_especie:
                a["especie"] = novo_especie
            if nova_raca:
                a["raca"] = nova_raca
            if nova_idade:
                a["idade"] = nova_idade
            if novo_sexo:
                a["sexo"] = novo_sexo
            if novo_estado:
                a["estado_saude"] = novo_estado
            if nova_data:
                a["data_chegada"] = nova_data
            if novo_comport:
                a["comportamento"] = novo_comport

            salvar_animais(animais)
            print(VERDE + "Animal atualizado!" + RESET)
            return

    print(VERMELHO + "Animal não encontrado." + RESET)


def obter_nome_animal(id_animal):
    """Retorna o nome do animal (ou None)."""
    animais = carregar_animais()
    for a in animais:
        if a["id"] == id_animal:
            return a["nome"]
    return None
