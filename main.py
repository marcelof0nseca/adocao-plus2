def cabecalho():
    arquivo_animais = open('animais.txt', 'a', encoding='utf-8')
    arquivo_animais.close()

    arquivo_animais = open('animais.txt', 'r', encoding='utf-8')
    conteudo = arquivo_animais.read()
    arquivo_animais.close()

    if conteudo.strip() == "":
        arquivo_animais = open('animais.txt', 'a', encoding='utf-8')
        arquivo_animais.write(f"|{'NOME':^12}|{'ESPÉCIE':^12}|{'RAÇA':^12}|{'IDADE':^7}|{'SEXO':^7}|{'ESTADO DE SAÚDE':^20}|{'DATA DE CHEGADA':^20}|{'COMPORTAMENTO':^18}|\n")
        arquivo_animais.close()


def organizarTexto(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


def adicionarAnimal():
    arquivo_animais = open('animais.txt', 'a', encoding='utf-8')

    nome = str(input('Digite o nome do animal: ')).capitalize()
    especie = str(input('Digite a espécie do animal: ')).capitalize()
    raca = str(input('Digite a raça do animal: ')).capitalize()
    idade = str(input('Digite a idade do animal: ')).capitalize()
    sexo = str(input('Digite o sexo do animal: ')).capitalize()
    estado = str(input('Digite o estado de saúde do animal: ')).capitalize()
    data = str(input('Digite a data de chegada do animal: '))
    comportamento = str(input('Digite o comportamento do animal: ')).capitalize()

    arquivo_animais.write(f'|{nome:^12}|{especie:^12}|{raca:^12}|{idade:^7}|{sexo:^7}|{estado:^20}|{data:^20}|{comportamento:^18}|\n')
    print('Animal cadastrado com sucesso!')
    arquivo_animais.close()


def visualizarAnimais():
    arquivo_animais = open('animais.txt', 'r', encoding='utf-8')
    print(arquivo_animais.read())
    arquivo_animais.close()


def editar_animal():
    arquivo = open('animais.txt', 'r', encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    if len(linhas) <= 1:
        print("Não existe nada a ser editado.")
        return  

    while True:
        print(f'{"ID":^3}\t{linhas[0].strip()}')  
        for i in range(1, len(linhas)):
            print(f'{i:^3}\t{linhas[i]}', end='')

        try:
            pergunta = int(input('1 - Excluir animal\n2 - Editar animal\n3 - Excluir lista completa\n4 - Encerrar\nDigite a opção desejada: '))
        except ValueError:
            print('Entrada inválida')
            continue

        if pergunta == 1:
            try:
                id_excluir = int(input('Digite o ID do animal para ser excluído: \n'))
                if 1 <= id_excluir < len(linhas):
                    del linhas[id_excluir]
                    arquivo = open('animais.txt', 'w', encoding="utf-8")
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print('Animal excluído com sucesso!')
                else:
                    print('ID inválido')
            except ValueError:
                print('Entrada inválida!')

        elif pergunta == 2:
            try:
                id_editar = int(input('Qual o ID do animal a ser editado: '))
                if 1 <= id_editar < len(linhas):
                    print('Digite os novos dados:')
                    nome = input('Nome: ').capitalize()
                    especie = input('Espécie: ').capitalize()
                    raca = input('Raça: ').capitalize()
                    idade = input('Idade: ').capitalize()
                    sexo = input('Sexo: ').capitalize()
                    estado = input('Estado de saúde: ').capitalize()
                    data = input('Data de chegada: ')
                    comportamento = input('Comportamento: ').capitalize()

                    nova = f'|{nome:^12}|{especie:^12}|{raca:^12}|{idade:^7}|{sexo:^7}|{estado:^20}|{data:^20}|{comportamento:^18}|\n'
                    linhas[id_editar] = nova

                    arquivo = open('animais.txt', 'w', encoding="utf-8")
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print('Animal editado com sucesso!')
                    visualizarAnimais()
                    return
                else:
                    print('ID inválido')
            except ValueError:
                print('Entrada inválida')

        elif pergunta == 3:
            conf = input('Tem certeza que deseja excluir toda a lista? [S/N]: ').upper()
            if conf == 'S':
                arquivo = open('animais.txt', 'w', encoding="utf-8")
                arquivo.close()
                cabecalho()
                print('Lista excluída com sucesso!')
                return
            else:
                print('Operação cancelada')

        elif pergunta == 4:
            print("Encerrando edição...")
            break

        else:
            print('Opção inválida.')

cabecalho()
print('Sistema de Gestão para Centros de Adoção de Animais')
while True:
    try:
        questionamento = int(input('1. Adicionar Animal\n2. Visualizar Animais\n3. Editar Animais\n4. Sair\nDigite a opção desejada: '))
    except ValueError:
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        continue
    except KeyboardInterrupt:
        print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        continue

    if questionamento == 1:
        adicionarAnimal()
    elif questionamento == 2:
        visualizarAnimais()
    elif questionamento == 3:
        editar_animal()
    elif questionamento == 4:
        print('Saindo...')
        break
    else:
        print('Digite uma opção válida!')
        