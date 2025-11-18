import os
from datetime import datetime



def _obter_caminho_arquivo(tipo: str) -> str:
    mapping = {
        'animais': 'animais.csv',
        'cuidados': 'cuidados.csv',
        'adocoes': 'adocoes.csv',
    }
    return mapping.get(tipo, f'{tipo}.csv')


def _cabecalhos_padrao(tipo: str):
    if tipo == 'animais':
        return ['id', 'nome', 'especie', 'raca', 'idade', 'sexo', 'estado_saude', 'data_chegada', 'comportamento']
    if tipo == 'cuidados':
        return ['id', 'animal_id', 'tipo', 'data_prevista', 'responsavel', 'status', 'observacoes']
    if tipo == 'adocoes':
        return ['id', 'animal_id', 'adotante_nome', 'data', 'observacoes']
    return ['id']


def _garantir_arquivo_e_cabecalho(tipo: str):
    path = _obter_caminho_arquivo(tipo)
    if not os.path.exists(path):
        headers = _cabecalhos_padrao(tipo)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(','.join(headers) + '\n')


def _gerar_id():
    # gera id baseado no timestamp atual (milissegundos)
    return datetime.now().strftime('%Y%m%d%H%M%S%f')


def _converter_animais_txt_se_preciso():
    txt_path = 'animais.txt'
    csv_path = _obter_caminho_arquivo('animais')
    if os.path.exists(csv_path):
        # csv already exists - nothing to do
        return
    if not os.path.exists(txt_path):
        return

    # tenta converter o formato tabular simples para CSV
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            linhas = [l.rstrip('\n') for l in f.readlines() if l.strip()]
        if not linhas:
            return

        header_line = linhas[0]
        # separa pelas barras verticais e remove espaços vazios
        tokens = [t.strip() for t in header_line.split('|') if t.strip()]
        headers = [t.lower().replace(' ', '_') for t in tokens]

        dados = []
        for linha in linhas[1:]:
            parts = [p.strip() for p in linha.split('|') if p.strip()]
            if not parts:
                continue
            # Se o número de campos bater com o header, mapeia, senão ignora
            if len(parts) == len(headers):
                registro = {headers[i]: parts[i] for i in range(len(headers))}
                registro.setdefault('id', _gerar_id())
                dados.append(registro)

        if dados:
            # escreve em CSV com cabeçalho padronizado
            csv_headers = _cabecalhos_padrao('animais')
            # adaptar campos existentes para o formato CSV esperado
            adaptados = []
            for d in dados:
                adaptado = {h: '' for h in csv_headers}
                adaptado['id'] = d.get('id', _gerar_id())
                adaptado['nome'] = d.get('nome', d.get('nOME', ''))
                adaptado['especie'] = d.get('espécie', d.get('especie', ''))
                adaptado['raca'] = d.get('raça', d.get('raca', ''))
                # tenta encontrar colunas que contenham 'idade', 'sexo', 'estado', 'data', 'comportamento'
                for k in d:
                    kl = k.lower()
                    if 'idade' in kl:
                        adaptado['idade'] = d[k]
                    if 'sexo' in kl:
                        adaptado['sexo'] = d[k]
                    if 'estado' in kl:
                        adaptado['estado_saude'] = d[k]
                    if 'data' in kl:
                        adaptado['data_chegada'] = d[k]
                    if 'comportamento' in kl:
                        adaptado['comportamento'] = d[k]
                adaptados.append(adaptado)

            # escreve CSV manualmente sem usar biblioteca externa
            with open(csv_path, 'w', encoding='utf-8') as f:
                f.write(','.join(csv_headers) + '\n')
                for reg in adaptados:
                    # substitui vírgulas nos campos por ponto-e-vírgula para evitar quebra
                    valores = [str(reg.get(h, '')).replace(',', ';') for h in csv_headers]
                    f.write(','.join(valores) + '\n')
    except Exception:
        # se ocorrer algum erro durante a conversão, não interrompe a execução
        return


def ler_dados(tipo: str):
    """Lê todos os registros do tipo e retorna lista de dicionários."""
    if tipo == 'animais':
        _converter_animais_txt_se_preciso()

    _garantir_arquivo_e_cabecalho(tipo)
    path = _obter_caminho_arquivo(tipo)
    registros = []
    with open(path, 'r', encoding='utf-8') as f:
        linhas = [l.rstrip('\n') for l in f.readlines()]
    if not linhas:
        return registros
    header = [h.strip() for h in linhas[0].split(',')]
    for linha in linhas[1:]:
        if not linha.strip():
            continue
        partes = [p.strip() for p in linha.split(',')]
        # mapeia cada coluna para o header (evita IndexError)
        reg = {}
        for i, h in enumerate(header):
            if i < len(partes):
                reg[h] = partes[i].replace(';', ',')
            else:
                reg[h] = ''
        registros.append(reg)
    return registros


def salvar_dados(tipo: str, dados) -> None:
    """Salva (append) um registro ou uma lista de registros do tipo.

    Se o registro não tiver campo 'id', será gerado um id baseado em timestamp.
    """
    _garantir_arquivo_e_cabecalho(tipo)
    path = _obter_caminho_arquivo(tipo)
    if isinstance(dados, dict):
        registros = [dados]
    else:
        registros = list(dados)

    # garante que todos os registros tenham id
    for r in registros:
        if 'id' not in r or r.get('id') in (None, ''):
            r['id'] = _gerar_id()

    # lê header atual
    with open(path, 'r', encoding='utf-8') as f:
        primeira = f.readline()
        headers = [h.strip() for h in primeira.rstrip('\n').split(',')] if primeira else _cabecalhos_padrao(tipo)

    with open(path, 'a', encoding='utf-8') as f:
        for r in registros:
            # escreve apenas as chaves que existem nos headers
            valores = []
            for h in headers:
                v = str(r.get(h, '')).replace(',', ';')
                valores.append(v)
            f.write(','.join(valores) + '\n')


def atualizar_dados(tipo: str, novos_dados) -> None:
    """Substitui todo o arquivo pelo `novos_dados` fornecido."""
    path = _obter_caminho_arquivo(tipo)
    headers = _cabecalhos_padrao(tipo)
    if novos_dados and isinstance(novos_dados, list):
        primeiro = novos_dados[0]
        if isinstance(primeiro, dict):
            headers = list(primeiro.keys())

    with open(path, 'w', encoding='utf-8') as f:
        f.write(','.join(headers) + '\n')
        for r in novos_dados:
            valores = [str(r.get(h, '')).replace(',', ';') for h in headers]
            f.write(','.join(valores) + '\n')
