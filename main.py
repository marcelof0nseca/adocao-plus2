from CrudAnimais import adicionar_animal, visualizar_animais, editar_animais, excluir_animal, AZUL,VERMELHO, RESET
from CadastroDeCuidados import cadastrar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa
from ContagemRegressiva import exibir_alertas, exibir_alertas_proximos
from Recomendador import recomendar_animal
from SugestoesPersonalizadas import main_sugestoes





def cabecalho():
    print(AZUL + "=== Sistema de Adoção ===" + RESET)

def menu():
    cabecalho()
    while True:
        print("\n1. Adicionar Animal")
        print("2. Visualizar Animais")
        print("3. Editar Animais")
        print("4. Cadastrar Tarefa")
        print("5. Listar Tarefas")
        print("6. Editar Tarefa")
        print("7. Excluir Tarefa")
        print("8. Visualizar Alertas")
        print("9. Verificar Alertas Proximos")
        print("10. Recomendar Animal")
        print("11. Sugestões Personalizadas")
        print("12. Excluir Animal")
        print("13. Sair")
        

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_animal()
        elif opcao == "2":
            visualizar_animais()
        elif opcao == "3":
            editar_animais()
        elif opcao == "4":
            cadastrar_tarefa()
        elif opcao == "5":
            listar_tarefas()
        elif opcao == "6":
            editar_tarefa()
        elif opcao == "7":
            excluir_tarefa()
        elif opcao == "8":
            exibir_alertas()
        elif opcao == "9":
            exibir_alertas_proximos()
        elif opcao == "10":
            recomendar_animal()
        elif opcao == "11":
            main_sugestoes()
        elif opcao == "12":
            excluir_animal()
        elif opcao == "13":
            print(AZUL + "Saindo..." + RESET)
            break
        else:
            print(VERMELHO + "Opção inválida!" + RESET)

if __name__ == "__main__":
    menu()
