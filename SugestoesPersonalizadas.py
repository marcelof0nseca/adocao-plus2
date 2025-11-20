def adocaointeligente():
    while True:
        pergunta=input('1 - para vizualizar adotantes\n2 - para adicionar adotantes\n3 - para editar arquivo\nPara encerrar digite [N]: ').lower()
        if pergunta=='n':
            break
        elif pergunta=='1':
            with open('adotantes.txt', 'r', encoding='utf-8') as arq:
                print(arq.read())
        elif pergunta == '2': 
                with open('adotantes.txt', 'a', encoding='utf-8') as arq:   
                    nome=input('digite o nome do adotante: ')
                    especie=input('digite a especie do animal: ')
                    idade_a=input('digite a idade do animal desejado: ')
                    raca_a=input('digite a raça do animal que você deseja: ')
                    sexo_a=input('digite a raça do animal que você deseja: ')
                    comportamento=input('digite a raça do animal que você deseja: ')
                    arq.write(f'|{nome:^12}|{especie:^12}|{raca_a:^12}|{idade_a:^7}|{sexo_a:^7}|{comportamento:^18}|\n')
        elif pergunta == '3': 
            try:
                with open('adotantes.txt', 'r', encoding='utf-8') as arq:
                    linhas=arq.readlines()
            except:
                    print('nada a ser editado')
            if len(linhas) < 1:
                print("Não existe nada a ser editado.")
                return  
                
            
                



while True:
    try:
        escolha=int(input('1 - adoção inteligente\n2 - cuidados especiais\n3 - compatibilidade com outros animais\n4 - atividades de socialização: '))
    except:
        print('Digite um numero inteiro')
    if escolha == 1:
        (adocaointeligente)
    elif escolha == 2:
        (cuidadosespeciais)
    elif escolha == 3:
        (compatiblidade)
    elif escolha == 4:
        (atv_socializacao)
    else:
        print('Opção inexistente ')
