from datetime import datetime, date
import os

def _normalizar_cabecalho(token: str) -> str:
    t = token.lower()
    replacements = {
        'ç': 'c', 'ã': 'a', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    t = t.replace(' ', '_')
    if 'nome' in t:
        return 'nome'
    if 'esp' in t:
        return 'especie'
    if 'raca' in t or ('ra' in t and 'r' in t):
        return 'raca'
    if 'idade' in t:
        return 'idade'
    if 'sexo' in t:
        return 'sexo'
    if 'estado' in t:
        return 'estado_saude'
    if 'chegada' in t or ('data' in t and 'prev' not in t):
        return 'data_chegada'
    if 'prev' in t or 'vac' in t or 'data_prevista' in t:
        return 'data_prevista'
    if 'comport' in t:
        return 'comportamento'
    if 'animal' in t and 'id' in t:
        return 'animal_id'
    if 'tipo' in t:
        return 'tipo'
    if 'respons' in t:
        return 'responsavel'
    if 'status' in t:
        return 'status'
    if 'observ' in t:
        return 'observacoes'
    if t == 'id':
        return 'id'
    return t

def _parse_table_txt(caminho: str):
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = [l.rstrip('\n') for l in f.readlines() if l.strip()]
    if not linhas:
        return []
    header = [t.strip() for t in linhas[0].split('|') if t.strip()]
    registros = []
    for linha in linhas[1:]:
        cols = [t.strip() for t in linha.split('|') if t.strip()]
        if not cols:
            continue
        reg = {}
        for i, h in enumerate(header):
            chave = _normalizar_cabecalho(h)
            reg[chave] = cols[i] if i < len(cols) else ''
        registros.append(reg)
    return registros

def _converter_para_data(data_str: str):
    if not data_str:
        return None
    formatos = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d"]
    for fmt in formatos:
        try:
            return datetime.strptime(data_str.strip(), fmt).date()
        except Exception:
            continue
    try:
        return datetime.fromisoformat(data_str.strip()).date()
    except Exception:
        return None

def dias_para_evento(data_evento: str):
    d = _converter_para_data(data_evento)
    if d is None:
        return None
    hoje = date.today()
    return (d - hoje).days

def exibir_alertas(id_animal: str):
    cuidados = _parse_table_txt('cuidados.txt')
    animais = _parse_table_txt('animais.txt')
    animal = next((a for a in animais if a.get('id') == id_animal or a.get('nome') == id_animal), None)
    nome = animal.get('nome', '<desconhecido>') if animal else id_animal
    eventos = [c for c in cuidados if c.get('animal_id') == id_animal or (animal and c.get('animal_id') == animal.get('id'))]
    if not eventos:
        print(f'Nenhum cuidado/tarefa cadastrado para o animal {nome} (id={id_animal}).')
        return
    print(f'Alertas para {nome} (id={id_animal}):')
    for ev in eventos:
        data = ev.get('data_prevista', '')
        dias = dias_para_evento(data)
        tipo = ev.get('tipo', 'tarefa')
        status = ev.get('status', '')
        if dias is None:
            print(f" - {tipo}: data inválida ('{data}'). Status: {status}")
        else:
            if dias < 0:
                print(f" - {tipo}: vencido há {-dias} dia(s) (data: {data}). Status: {status}")
            elif dias == 0:
                print(f" - {tipo}: hoje (data: {data}). Status: {status}")
            else:
                print(f" - {tipo}: daqui a {dias} dia(s) (data: {data}). Status: {status}")

def verificar_alertas_proximos(days: int = 7):
    cuidados = _parse_table_txt('cuidados.txt')
    proximos = []
    for ev in cuidados:
        data = ev.get('data_prevista', '')
        dias = dias_para_evento(data)
        if dias is None:
            continue
        if 0 <= dias <= days:
            proximos.append({
                'animal_id': ev.get('animal_id'),
                'tipo': ev.get('tipo'),
                'data_prevista': data,
                'dias_restantes': dias,
                'status': ev.get('status', '')
            })
    return proximos

if __name__ == '__main__':
    proximos = verificar_alertas_proximos(7)
    if not proximos:
        print('Nenhum alerta próximo em 7 dias.')
    else:
        for p in proximos:
            print(f"Animal {p['animal_id']}: {p['tipo']} em {p['dias_restantes']} dia(s) ({p['data_prevista']})")
            def verificar_alertas_proximos(days=7):
                cuidados = _parse_table_txt('cuidados.txt')
                proximos = []
                for ev in cuidados:
                    data = ev.get('data_prevista', '')
                    dias = dias_para_evento(data)
                    if dias is None:
                        continue
                    if 0 <= dias <= days:
                        proximos.append({
                            'animal_id': ev.get('animal_id'),
                            'tipo': ev.get('tipo'),
                            'data_prevista': data,
                            'dias_restantes': dias,
                            'status': ev.get('status', '')
                        })
                return proximos
            for p in proximos:
                print(f"Animal {p['animal_id']}: {p['tipo']} em {p['dias_restantes']} dia(s) ({p['data_prevista']})")
            for p in proximos:
                print(f"Animal {p['animal_id']}: {p['tipo']} em {p['dias_restantes']} dia(s) ({p['data_prevista']})")
            for p in proximos:
                print(f"Animal {p['animal_id']}: {p['tipo']} em {p['dias_restantes']} dia(s) ({p['data_prevista']})")
            exibir_alertas(p['animal_id'])
