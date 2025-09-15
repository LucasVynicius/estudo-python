def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return


def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else "Pendente"
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return


def atualizar_tarefa(tarefas, indice, novo_nome):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):    
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome
        print(f"Tarefa {indice} atualizada com sucesso!")
    else:
        print("Índice inválido. Nenhuma tarefa foi atualizada.")
    return


def completar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice} marcada como completada!")
    return


def deletar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefa_removida = tarefas.pop(indice_tarefa_ajustado)
        print(f"Tarefa '{tarefa_removida['tarefa']}' deletada com sucesso!")
    else:
        print("Índice inválido. Nenhuma tarefa foi deletada.")
    return


tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa:")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice)
    elif escolha == "5":
        tarefas = [tarefa for tarefa in tarefas if not tarefa["completada"]]
        print("Tarefas completadas foram deletadas com sucesso!")
    elif escolha == "6":
        print("Saindo do gerenciador de tarefas. Até mais!")
        break
