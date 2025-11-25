ARQUIVO_ANIMAIS = "animais.txt"

VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'


def carregar_animais():
    animais = []
    try:
        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 9:
                    continue
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
    except FileNotFoundError:
        pass

    return animais


def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arq:
        for a in animais:
            arq.write(
                f"{a['id']};{a['nome']};{a['especie']};{a['raca']};"
                f"{a['idade']};{a['sexo']};{a['estado_saude']};"
                f"{a['data_chegada']};{a['comportamento']}\n"
            )



def _proximo_id(animais):
    if not animais:
        return 1
    return max(a["id"] for a in animais) + 1


def id_existe_animal(id_animal):
    for a in carregar_animais():
        if a["id"] == id_animal:
            return True
    return False


def obter_nome_animal(id_animal):
    for a in carregar_animais():
        if a["id"] == id_animal:
            return a["nome"]
    return None


def adicionar_animal():
    animais = carregar_animais()
    novo_id = _proximo_id(animais)

    print(AZUL + f"\nID gerado automaticamente: {novo_id}" + RESET)

    nome = input("Nome: ").strip()
    especie = input("Espécie: ").strip()
    raca = input("Raça: ").strip()
    idade = input("Idade: ").strip()
    sexo = input("Sexo: ").strip()
    estado_saude = input("Estado de Saúde: ").strip()
    data_chegada = input("Data de Chegada (DD/MM/AAAA): ").strip()
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
    print(VERDE + "\nAnimal cadastrado com sucesso!" + RESET)


def visualizar_animais():
    animais = carregar_animais()

    if not animais:
        print(VERMELHO + "\nNenhum animal cadastrado." + RESET)
        return

    print(AZUL + "\n=== LISTA DE ANIMAIS ===" + RESET)
    for a in animais:
        print(
            f"ID: {a['id']} | Nome: {a['nome']} | Espécie: {a['especie']} | Raça: {a['raca']} | "
            f"Idade: {a['idade']} | Sexo: {a['sexo']} | Estado: {a['estado_saude']} | "
            f"Chegada: {a['data_chegada']} | Comportamento: {a['comportamento']}"
        )


def editar_animais():
    animais = carregar_animais()

    if not animais:
        print(VERMELHO + "\nNenhum animal cadastrado." + RESET)
        return

    visualizar_animais()

    try:
        id_edit = int(input("\nID do animal que deseja editar: ").strip())
    except:
        print(VERMELHO + "ID inválido!" + RESET)
        return

    for a in animais:
        if a["id"] == id_edit:

            print(AMARELO + "\nDeixe qualquer campo em branco para manter o valor atual.\n" + RESET)

            nome = input(f"Nome [{a['nome']}]: ").strip()
            especie = input(f"Espécie [{a['especie']}]: ").strip()
            raca = input(f"Raça [{a['raca']}]: ").strip()
            idade = input(f"Idade [{a['idade']}]: ").strip()
            sexo = input(f"Sexo [{a['sexo']}]: ").strip()
            estado = input(f"Estado de Saúde [{a['estado_saude']}]: ").strip()
            chegada = input(f"Data de Chegada [{a['data_chegada']}]: ").strip()
            comport = input(f"Comportamento [{a['comportamento']}]: ").strip()

            if nome: a["nome"] = nome
            if especie: a["especie"] = especie
            if raca: a["raca"] = raca
            if idade: a["idade"] = idade
            if sexo: a["sexo"] = sexo
            if estado: a["estado_saude"] = estado
            if chegada: a["data_chegada"] = chegada
            if comport: a["comportamento"] = comport

            salvar_animais(animais)
            print(VERDE + "\nAnimal atualizado com sucesso!" + RESET)
            return

    print(VERMELHO + "\nAnimal não encontrado." + RESET)


def excluir_animal():
    animais = carregar_animais()

    if not animais:
        print(VERMELHO + "\nNenhum animal cadastrado." + RESET)
        return

    visualizar_animais()

    try:
        id_del = int(input("\nID do animal que deseja excluir: ").strip())
    except:
        print(VERMELHO + "ID inválido!" + RESET)
        return

    for a in animais:
        if a["id"] == id_del:
            confirma = input(f"Tem certeza que deseja excluir o animal '{a['nome']}'? (s/n): ").strip().lower()
            if confirma != "s":
                print(AMARELO + "Ação cancelada." + RESET)
                return

            animais.remove(a)
            salvar_animais(animais)
            print(VERDE + "\nAnimal excluído com sucesso!" + RESET)
            return

    print(VERMELHO + "\nAnimal não encontrado." + RESET)
