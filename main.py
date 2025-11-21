from CrudAnimais import adicionar_animal, visualizar_animais, editar_animais, AZUL,VERMELHO, RESET
from CadastroDeCuidados import cadastrar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa
from ContagemRegressiva import exibir_alertas, verificar_alertas_proximos
from recomendador import recomendar_animal




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
        print("9. Recomendar Animal")
        print("10. Sair")
        

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
            recomendar_animal()
        elif opcao == "10":
            break
        
        
        else:
            print(VERMELHO + "Opção inválida!" + RESET)

if __name__ == "__main__":
    menu()
