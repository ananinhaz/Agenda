# Programa de Agenda de Compromissos

from datetime import datetime, timedelta

# Lista para armazenar os compromissos
agenda = []

# Função para adicionar um compromisso único
def adicionar_compromisso():
    data = input("Digite a data do compromisso (dd/mm/aaaa): ")
    hora = input("Digite a hora do compromisso (hh:mm): ")
    descricao = input("Digite a descrição do compromisso: ")
    local = input("Digite o local do compromisso: ")
    
    # Perguntar quando quer ser lembrado
    lembrete = input("Com quantos minutos de antecedência deseja ser lembrado? (Digite 0 para nenhum lembrete): ")
    
    compromisso = {
        'data': data,
        'hora': hora,
        'descricao': descricao,
        'local': local,
        'lembrete': int(lembrete)  # Armazena o lembrete como um número inteiro de minutos
    }
    
    # Verificar conflito de horário antes de adicionar
    if verificar_conflito(compromisso):
        print("Aviso: Existe um compromisso no mesmo dia e horário!\n")
    
    agenda.append(compromisso)
    print("Compromisso adicionado com sucesso!\n")

# Função para adicionar compromissos em um período de tempo
def adicionar_evento_periodo():
    descricao = input("Digite a descrição do evento: ")
    data_inicio = input("Digite a data de início do evento (dd/mm/aaaa): ")
    data_fim = input("Digite a data de fim do evento (dd/mm/aaaa): ")
    
    evento = {
        'descricao': descricao,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    }
    
    agenda.append(evento)
    print("Evento de período adicionado com sucesso!\n")

# Função para listar todos os compromissos e eventos
def listar_compromissos():
    if not agenda:
        print("Nenhum compromisso agendado.\n")
    else:
        print("Lista de compromissos:")
        for idx, compromisso in enumerate(agenda):
            if 'hora' in compromisso:
                print(f"{idx + 1}. Data: {compromisso['data']}, Hora: {compromisso['hora']}")
                print(f"   Descrição: {compromisso['descricao']}, Local: {compromisso['local']}")
                print(f"   Lembrete: {compromisso['lembrete']} minutos antes\n")
            else:
                print(f"{idx + 1}. Evento: {compromisso['descricao']}")
                print(f"   Início: {compromisso['data_inicio']}, Fim: {compromisso['data_fim']}\n")

# Função para excluir um compromisso ou evento
def excluir_compromisso():
    listar_compromissos()
    if agenda:
        try:
            indice = int(input("Digite o número do compromisso que deseja excluir: ")) - 1
            if 0 <= indice < len(agenda):
                agenda.pop(indice)
                print("Compromisso excluído com sucesso!\n")
            else:
                print("Número inválido!\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

# Função para verificar se há compromissos no mesmo horário e dia
def verificar_conflito(novo_compromisso):
    for compromisso in agenda:
        if 'hora' in compromisso:
            if (compromisso['data'] == novo_compromisso['data'] and 
                compromisso['hora'] == novo_compromisso['hora']):
                return True
    return False

# Função para listar compromissos de um dia específico
def listar_compromissos_do_dia():
    data = input("Digite a data para listar os compromissos (dd/mm/aaaa): ")
    compromissos_do_dia = [compromisso for compromisso in agenda if compromisso.get('data') == data]
    
    if compromissos_do_dia:
        print(f"Compromissos para o dia {data}:")
        for compromisso in compromissos_do_dia:
            print(f" - {compromisso['hora']} - {compromisso['descricao']} no {compromisso['local']}")
            print(f"   Lembrete: {compromisso['lembrete']} minutos antes\n")
    else:
        print(f"Não há compromissos para o dia {data}.\n")

# Função principal para o menu de opções
def menu():
    while True:
        print("Agenda de Compromissos")
        print("1. Adicionar Compromisso")
        print("2. Adicionar Evento em Período")
        print("3. Listar Compromissos")
        print("4. Listar Compromissos do Dia")
        print("5. Excluir Compromisso")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_compromisso()
        elif opcao == '2':
            adicionar_evento_periodo()
        elif opcao == '3':
            listar_compromissos()
        elif opcao == '4':
            listar_compromissos_do_dia()
        elif opcao == '5':
            excluir_compromisso()
        elif opcao == '6':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

# Executa o programa
menu()