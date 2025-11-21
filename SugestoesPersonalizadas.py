def adocaointeligente():
    while True:
        pergunta = input(
            '\n1 - para visualizar adotantes\n2 - para adicionar adotantes\n3 - para remover adotantes\nPara encerrar digite [N]: '
        ).lower()

        if pergunta == 'n':
            break

        elif pergunta == '1':
            try:
                with open('adotantes.txt', 'r', encoding='utf-8') as arq:
                    linhas = arq.readlines()
                    if not linhas:
                        print("Nenhum adotante cadastrado.")
                    else:
                        print("\n--- Lista de adotantes ---")
                        for i, linha in enumerate(linhas, start=1):
                            print(f"ID {i}: {linha.strip()}")
            except FileNotFoundError:
                print("Nenhum arquivo encontrado.")

        elif pergunta == '2':
            with open('adotantes.txt', 'a', encoding='utf-8') as arq:
                nome = input('Digite o nome do adotante: ')
                especie = input('Digite a espécie do animal: ')
                idade_a = input('Digite a idade do animal desejado: ')
                raca_a = input('Digite a raça do animal que você deseja: ')
                sexo_a = input('Digite o sexo do animal que você deseja: ')
                comportamento = input('Digite o comportamento do animal que você deseja: ')
                arq.write(f'|{nome:^12}|{especie:^12}|{raca_a:^12}|{idade_a:^7}|{sexo_a:^7}|{comportamento:^18}|\n')
            print("Adotante adicionado com sucesso!")

        elif pergunta == '3':
            try:
                with open('adotantes.txt', 'r', encoding='utf-8') as arq:
                    linhas = arq.readlines()
                if not linhas:
                    print("Não existe nada a ser removido.")
                    continue

                print("\n--- Lista de adotantes ---")
                id=1
                for linha in linhas:
                    print(f"ID {id}: {linha.strip()}")
                    id=id+1

                try:
                    remover_id = int(input("Digite o ID do adotante que já adotou e deve ser removido: "))
                    if 1 <= remover_id <= len(linhas):
                        linhas.pop(remover_id - 1)
                        with open('adotantes.txt', 'w', encoding='utf-8') as arq:
                            arq.writelines(linhas)
                        print("Adotante removido com sucesso!")
                    else:
                        print("ID inválido.")
                except ValueError:
                    print("Digite um número válido para o ID.")
            except FileNotFoundError:
                print("Nada a ser editado.")


def cuidadosespeciais():
    print("\n--- Cuidados Especiais ---")
    especie = input("Digite a espécie do animal (cachorro/gato/outro): ").lower()
    try:
        idade = int(input("Digite a idade do animal: "))
    except ValueError:
        print("Idade inválida.")
        return

    if especie == "cachorro":
        if idade < 2:
            print("Cuidados: vacinas em dia, alimentação para filhotes, bastante brincadeira.")
        elif idade < 8:
            print("Cuidados: passeios regulares, alimentação adequada, visitas ao veterinário anuais.")
        else:
            print("Cuidados: check-ups frequentes, alimentação especial para idosos, atividades leves.")
    elif especie == "gato":
        if idade < 2:
            print("Cuidados: caixa de areia limpa, vacinas, brinquedos para gastar energia.")
        elif idade < 10:
            print("Cuidados: alimentação balanceada, arranhadores, visitas regulares ao veterinário.")
        else:
            print("Cuidados: atenção à mobilidade, consultas frequentes, ambiente tranquilo.")
    else:
        print("Cuidados gerais: alimentação adequada, higiene e acompanhamento veterinário.")


def compatibilidade():
    print("\n--- Compatibilidade com outros animais ---")
    temperamento = input("O cachorro é agressivo ou manso? ").lower()
    sexo = input("O cachorro é macho ou fêmea? ").lower()

    if temperamento == "agressivo":
        print("Recomendação: socialização gradual, evitar contato imediato com outros animais, acompanhamento de adestrador.")
    elif temperamento == "manso":
        print("Recomendação: pode conviver com outros animais, introdução supervisionada e ambiente tranquilo.")
    else:
        print("Temperamento não identificado, recomenda-se avaliação com especialista.")

    if sexo == "macho":
        print("Atenção: machos podem disputar território, especialmente com outros machos.")
    elif sexo == "fêmea":
        print("Fêmeas geralmente se adaptam melhor, mas cada caso deve ser avaliado.")
    else:
        print("Sexo não identificado.")


def atv_socializacao():
    print("\n--- Atividades de Socialização ---")
    caso = input("Digite o caso (filhote/adulto/agressivo/tímido): ").lower()

    if caso == "filhote":
        print("Exemplo: levar para parques, brincar com outros filhotes, aulas de adestramento básico.")
    elif caso == "adulto":
        print("Exemplo: passeios regulares, encontros controlados com outros cães, atividades de obediência.")
    elif caso == "agressivo":
        print("Exemplo: socialização gradual, uso de guia e focinheira, acompanhamento profissional.")
    elif caso == "tímido":
        print("Exemplo: introdução lenta a novos ambientes, reforço positivo, convívio com animais calmos.")
    else:
        print("Caso não identificado, recomenda-se observar o comportamento e adaptar as atividades.")


while True:
    try:
        escolha = int(input(
            '\n1 - adoção inteligente\n2 - cuidados especiais\n3 - compatibilidade com outros animais\n4 - atividades de socialização\nDigite sua escolha: '
        ))
    except ValueError:
        print('Digite um número inteiro.')
        continue

    if escolha == 1:
        adocaointeligente()
    elif escolha == 2:
        cuidadosespeciais()
    elif escolha == 3:
        compatibilidade()
    elif escolha == 4:
        atv_socializacao()
    else:
        print('Opção inexistente.')