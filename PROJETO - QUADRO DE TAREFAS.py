#PROJETO DE QUADRO DE TAREFAS

#1- Adicionar Tarefas: Permitir ao usuário adicionar uma nova tarefa.
#2- Visualizar Tarefas: Mostrar todas as tarefas adicionadas.
#3- Remover Tarefas: Permitir ao usuário remover uma tarefa pelo seu índice.

quadro_de_tarefas = []

def adicionar_tarefa():
    tarefa = input('Qual tarefa deseja adicionar ao quadro?: ')
    #Adicionando a tarefa dentro da lista
    quadro_de_tarefas.append(tarefa)
    print(f'Tarefa"{tarefa}" adicionada ao quadro.')


def visualizar_tarefas():
    #Verificando se a lista esta vazia
    if quadro_de_tarefas:
        print('Tarefas no quadro:')
        #Utilizando o indice e enumerate para numerar todas as tarefas de acordo com seus respectivos indices. Começando por 1
        for indice, tarefa in enumerate(quadro_de_tarefas, start=1):
            print(f'{indice}. {tarefa}')
    else:
        print('Nenhuma tareda no quadro')


def remover_tarefa():
    if quadro_de_tarefas:
        #Verificando se a lista está vazia
        visualizar_tarefas()
        try:
            #Tentando executar o codigo abaixo
            indice = int(input('Digite o numero de taredas que deseja remover: '))
            if 1 <= indice <= len(quadro_de_tarefas):
                #Caso 1 seja menor ou igual ao indice, e indice for menor ou igual ao tamanho da lista.
                tarefa_removida = quadro_de_tarefas.pop(indice - 1)
                print(f'tareda "{tarefa_removida}" removida do quadro')
            else:
                print('Indice invalido.')
                #Caso ocorra um erro, o programa identifica
        except ValueError:
            print('Por favor, insira um numero valido.')
    else:
        print('Nenhuma tarefa para remover.')

#Loop para o usuario escolher oq fazer
while True:
    print('\nMenu:')
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        adicionar_tarefa()
    elif escolha == '2':
        visualizar_tarefas()
    elif escolha == '3':
        remover_tarefa()
    elif escolha == '4':
        print('Saindo...')
        break
    else:
        print('Opção invalida. Por favor, escolha uma opção valida.')



