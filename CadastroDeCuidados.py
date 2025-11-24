from CrudAnimais import id_existe_animal, obter_nome_animal, VERDE, VERMELHO, AMARELO, RESET

ARQUIVO_CUIDADOS = "cuidados.txt"


def carregar_cuidados():
    cuidados = []
    try:
        with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                partes = linha.split(";")
                if len(partes) != 4:   
                    continue

                try:
                    cuidados.append({
                        "id_animal": int(partes[0]),
                        "descricao": partes[1],
                        "data_prevista": partes[2],
                        "responsavel": partes[3],
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        return []

    return cuidados


def salvar_cuidados(cuidados):
    with open(ARQUIVO_CUIDADOS, "w", encoding="utf-8") as arq:
        for c in cuidados:
            arq.write(
                f"{c['id_animal']};{c['descricao']};{c['data_prevista']};{c['responsavel']}\n"
            )


def cadastrar_tarefa():
    cuidados = carregar_cuidados()

    try:
        id_animal = int(input("ID do animal: ").strip())
    except ValueError:
        print(VERMELHO + "ID inválido!" + RESET)
        return

    if not id_existe_animal(id_animal):
        print(VERMELHO + "Esse animal não existe!" + RESET)
        return

    descricao = input("Descrição da tarefa: ").strip()
    data = input("Data prevista (DD/MM/AAAA): ").strip()
    responsavel = input("Responsável: ").strip()

    cuidados.append({
        "id_animal": id_animal,
        "descricao": descricao,
        "data_prevista": data,
        "responsavel": responsavel,
    })

    salvar_cuidados(cuidados)
    print(VERDE + "Tarefa cadastrada com sucesso!" + RESET)


def listar_tarefas(id_animal=None):
    cuidados = carregar_cuidados()

    if not cuidados:
        print(VERMELHO + "Nenhuma tarefa cadastrada." + RESET)
        return {}

    print(AMARELO + "\n===== LISTA DE TAREFAS =====" + RESET)

    mapa = {}
    contador = 1

    for i, c in enumerate(cuidados):
        if id_animal is not None and c["id_animal"] != id_animal:
            continue

        mapa[contador] = i

        nome = obter_nome_animal(c["id_animal"]) or "Desconhecido"

        print(f"[{contador}] Animal: {nome} (ID {c['id_animal']})")
        print(f"     Descrição: {c['descricao']}")
        print(f"     Data prevista: {c['data_prevista']}")
        print(f"     Responsável: {c['responsavel']}\n")

        contador += 1

    return mapa


def excluir_tarefa():
    cuidados = carregar_cuidados()

    if not cuidados:
        print(VERMELHO + "Nenhuma tarefa para excluir." + RESET)
        return

    mapa = listar_tarefas()

    try:
        idx_user = int(input("Digite o número da tarefa a excluir: ").strip())
    except ValueError:
        print(VERMELHO + "Entrada inválida." + RESET)
        return

    if idx_user not in mapa:
        print(VERMELHO + "Índice fora do intervalo." + RESET)
        return

    idx_real = mapa[idx_user]  
    removida = cuidados.pop(idx_real)

    salvar_cuidados(cuidados)

    nome = obter_nome_animal(removida["id_animal"]) or "Desconhecido"
    print(VERDE + f"Tarefa removida: {nome} - {removida['descricao']}" + RESET)



def editar_tarefa():
    cuidados = carregar_cuidados()

    if not cuidados:
        print(VERMELHO + "Nenhuma tarefa para editar." + RESET)
        return

    mapa = listar_tarefas()

    try:
        idx_user = int(input("Digite o número da tarefa a editar: ").strip())
    except ValueError:
        print(VERMELHO + "Entrada inválida!" + RESET)
        return

    if idx_user not in mapa:
        print(VERMELHO + "Índice fora do intervalo!" + RESET)
        return

    idx_real = mapa[idx_user]
    tarefa = cuidados[idx_real]

    print("Deixe vazio para manter o valor atual.")

    nova_desc = input(f"Nova descrição [{tarefa['descricao']}]: ").strip()
    nova_data = input(f"Nova data [{tarefa['data_prevista']}]: ").strip()
    novo_resp = input(f"Novo responsável [{tarefa['responsavel']}]: ").strip()

    if nova_desc:
        tarefa["descricao"] = nova_desc
    if nova_data:
        tarefa["data_prevista"] = nova_data
    if novo_resp:
        tarefa["responsavel"] = novo_resp

    salvar_cuidados(cuidados)
    print(VERDE + "Tarefa atualizada com sucesso!" + RESET)
