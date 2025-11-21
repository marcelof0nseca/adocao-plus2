from CrudAnimais import id_existe_animal, obter_nome_animal, VERDE, VERMELHO, AMARELO, RESET

ARQUIVO_CUIDADOS = "cuidados.txt"
DATE_FORMAT = "%d/%m/%Y"


def carregar_cuidados():
    cuidados = []
    try:
        with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                if len(partes) < 4:
                    continue
                try:
                    cuidados.append({
                        "id_animal": int(partes[0]),
                        "descricao": partes[1],
                        "data_prevista": partes[2],
                        "responsavel": partes[3],
                    })
                except:
                    continue
    except FileNotFoundError:
        pass
    return cuidados


def salvar_cuidados(cuidados):
    with open(ARQUIVO_CUIDADOS, "w", encoding="utf-8") as arq:
        for c in cuidados:
            arq.write(f"{c['id_animal']};{c['descricao']};{c['data_prevista']};{c['responsavel']}\n")


def cadastrar_tarefa():
    cuidados = carregar_cuidados()

    try:
        id_animal = int(input("ID do animal: ").strip())
    except:
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
        return

    print(AMARELO + "\n===== LISTA DE TAREFAS =====" + RESET)
    for idx, c in enumerate(cuidados, start=1):
        if id_animal is not None and c["id_animal"] != id_animal:
            continue
        nome = obter_nome_animal(c["id_animal"]) or "Desconhecido"
        print(f"[{idx}] Animal: {nome} (ID {c['id_animal']})")
        print(f"     Descrição: {c['descricao']}")
        print(f"     Data prevista: {c['data_prevista']}")
        print(f"     Responsável: {c['responsavel']}\n")


def excluir_tarefa():
    cuidados = carregar_cuidados()
    if not cuidados:
        print(VERMELHO + "Nenhuma tarefa para excluir." + RESET)
        return

    listar_tarefas()
    try:
        idx = int(input("Digite o número da tarefa a excluir (ex: 1): ").strip())
    except:
        print(VERMELHO + "Entrada inválida." + RESET)
        return

    if idx < 1 or idx > len(cuidados):
        print(VERMELHO + "Índice fora do intervalo." + RESET)
        return

    apagado = cuidados.pop(idx - 1)
    salvar_cuidados(cuidados)
    nome = obter_nome_animal(apagado["id_animal"]) or "Desconhecido"
    print(VERDE + f"Tarefa removida: {nome} - {apagado['descricao']}" + RESET)


def editar_tarefa():
    cuidados = carregar_cuidados()
    if not cuidados:
        print(VERMELHO + "Nenhuma tarefa para editar." + RESET)
        return

    listar_tarefas()
    try:
        idx = int(input("Digite o número da tarefa a editar (ex: 1): ").strip())
    except:
        print(VERMELHO + "Entrada inválida." + RESET)
        return

    if idx < 1 or idx > len(cuidados):
        print(VERMELHO + "Índice fora do intervalo." + RESET)
        return

    tarefa = cuidados[idx - 1]
    print("Deixe em branco para manter o valor atual.")

    try:
        novo_id_animal_str = input(f"Novo ID do animal [{tarefa['id_animal']}]: ").strip()
        if novo_id_animal_str:
            novo_id_animal = int(novo_id_animal_str)
            if not id_existe_animal(novo_id_animal):
                print(VERMELHO + "Animal inexistente." + RESET)
                return
            tarefa['id_animal'] = novo_id_animal
    except:
        print(VERMELHO + "ID inválido." + RESET)
        return

    nova_desc = input(f"Nova descrição [{tarefa['descricao']}]: ").strip()
    nova_data = input(f"Nova data [{tarefa['data_prevista']}]: ").strip()
    novo_resp = input(f"Novo responsável [{tarefa['responsavel']}]: ").strip()

    if nova_desc:
        tarefa['descricao'] = nova_desc
    if nova_data:
        tarefa['data_prevista'] = nova_data
    if novo_resp:
        tarefa['responsavel'] = novo_resp

    salvar_cuidados(cuidados)
    print(VERDE + "Tarefa atualizada!" + RESET)
