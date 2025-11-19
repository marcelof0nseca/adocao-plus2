from datetime import datetime, date
from CrudAnimais import obter_nome_animal, VERDE, VERMELHO, AMARELO, AZUL, RESET
from CadastroDeCuidados import carregar_cuidados


def _converter_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date()
    except:
        return None


def dias_para(data_str):
    d = _converter_data(data_str)
    if not d:
        return None
    hoje = date.today()
    return (d - hoje).days


def exibir_alertas():
    cuidados = carregar_cuidados()

    if not cuidados:
        print(VERMELHO + "Nenhum cuidado cadastrado." + RESET)
        return

    print(AZUL + "\n======= ALERTAS DE CUIDADOS =======" + RESET)

    for c in cuidados:
        nome = obter_nome_animal(c["id_animal"]) or "Desconhecido"
        dias = dias_para(c["data_prevista"])

        if dias is None:
            cor = VERMELHO
            msg = "Data inválida"
        elif dias < 0:
            cor = VERMELHO
            msg = f"ATRASADO há {-dias} dia(s)"
        elif dias == 0:
            cor = AMARELO
            msg = "É HOJE!"
        elif dias <= 7:
            cor = AMARELO
            msg = f"Falta {dias} dia(s)"
        else:
            cor = VERDE
            msg = f"Falta {dias} dia(s)"

        print(cor + f"Animal: {nome} (ID {c['id_animal']})" + RESET)
        print(f"  Tarefa: {c['descricao']}")
        print(f"  Responsável: {c['responsavel']}")
        print(f"  Data prevista: {c['data_prevista']}  →  {msg}\n")
    


def verificar_alertas_proximos(dias_limite=7):
    cuidados = carregar_cuidados()
    proximos = []

    for c in cuidados:
        dias = dias_para(c["data_prevista"])
        if dias is None:
            continue
        if 0 <= dias <= dias_limite:
            proximos.append({
                "id_animal": c["id_animal"],
                "nome": obter_nome_animal(c["id_animal"]) or "Desconhecido",
                "descricao": c["descricao"],
                "responsavel": c["responsavel"],
                "data_prevista": c["data_prevista"],
                "dias_restantes": dias
            })

    return proximos
