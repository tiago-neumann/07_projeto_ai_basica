"""import json - Permite trabalhar com dados de arquivos JSON"""
"""from datetime import datetime - Permite trabalhar com datas"""
"""import time - Permite trabalhar com tempos, como pausar e etc..."""
"""import os - Permite interagir e puxar informações do sistema operacional do próprio computador"""

import json
from datetime import datetime
import time
import os

"""data - Pega a data atual, 'datetime.now()' pega a data de hoje/agora, '.strftime()' transforma a data em texto, formatando ela na ordem imposta"""

data = datetime.now().strftime("%d/%m/%y")

"""pasta_atual - Como o nome diz ele reconhece qual é o caminho da pasta atual"""
"""os.path.dirname - Ele pega o caminho completo e deixa apenas o caminho até a pasta, sem o nome do arquivo atual"""
"""os.path.abspath - Ele pega o caminho completo onde o arquivo atual (__file__) esta localizado"""

pasta_atual = os.path.dirname(os.path.abspath(__file__))

"""caminho - Ele junta pelo 'os.path.join' o caminho da pasta atual, com o arquivo JSON que desejamos acessar"""

caminho = os.path.join(pasta_atual, "despesas.json")

#=====================
#Função de Limpar a Tela
#=====================

"""def limpar_tela() - Cria uma função que pode ser chamada depois"""
"""os.system('cls'...) - Executa a limpeza de dados do terminal, 'os.system' permite executar comando no sistema operacional, 'cls' é o comando de limpar"""

def limpar_tela():
    os.system('cls')

#=====================
#Função para Avisos
#=====================

"""def aviso(texto) - A diferença nessa função é que ela tem um paramêtro que pode ser declarado quando chamada"""
"""time.sleep(1) - Ele vem do 'import time', dando uma pausa de um segundo no sistema, para depois continuar"""

def aviso(texto):
    limpar_tela()
    print(f"\n{texto}")
    time.sleep(1)
    limpar_tela()

#=====================
#Função de Criação de Lista
#=====================

"""with open(caminho...) - Ele abre o arquivo, podendo pegar dados do arquivo json"""
"""with - Meio que cuida do início e do fim da operação, fazendo uma limpeza automática quando sai do bloco"""
"""open - Ela abre o caminho do arquivo"""
"""'r' - Significa 'read' de ler, no caso ele lê o arquivo"""
"""encoding='utf=8' - Permite que o sistema entenda o acentos e letras de diferentes idiomas, além do inglês"""
"""as arquivo - Serve meio meio que como uma variável que guarda esse 'open(...)'"""
"""desepesas = json.load(arquivo) - Cria uma variável que toda vez chamada carrega o json do caminho posto dentro da variável arquivo"""

"""for item in despesas - Significa que para o 'item' (que pode ser um nome qualquer) rode o a variável despesas até acabar"""
"""Ai ele vai escrevendo os dados que ele vai passando, na tela, ai vai repetindo até chegar no fim do arquivo"""

def lista():

    with open(caminho, "r", encoding="utf=8") as arquivo:
        despesas = json.load(arquivo)

    for item in despesas:
        print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']}R$ | Categoria: {item['Categoria']}")

#=====================
#Função de Título
#=====================

def titulo(texto):
    print("\n================================")
    print(f"{texto}")
    print("================================\n")

#=====================
#Função de Exibir Menu
#=====================

def menu():

    limpar_tela()

    while True:
        titulo("GERENCIADOR DE DESPESAS")
        print("1. Cadastrar despesa") 
        print("2. Listar despesas")
        print("3. Editar despesa")
        print("4. Excluir despesa")
        print("5. Ver gastos por categoria")
        print("6. Ver total")
        print("7. Salvar e sair")
        print("\n================================\n")

        opcao = input("Escolha uma opção: ")

        limpar_tela()

        if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8"]:  
            aviso("INSIRA UM VALOR VÁLIDO!!!")
        else:
            escolhas(opcao)
            return True



#=====================
#Função de Cadastrar Despesas
#=====================

def cadastrar():

    titulo("CADASTRO DE DESPESAS")

    nome = input("- Digite o nome da despesa: ")
    valor = input("- Digite o valor da despesa: ")
    categoria = input("- Digite a categoria da despesa: ")

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf=8") as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []

    if dados:
        novo_id = max(item["ID"] for item in dados) + 1
    else:
        novo_id = 1

    nova_despesa = {
        "ID": novo_id,
        "Nome": nome,
        "Valor": valor,
        "Categoria": categoria,
        "Data": data
    }

    
    dados.append(nova_despesa)

    with open(caminho, "w", encoding="utf=8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    aviso("DESPESA CADASTRADA")

    menu()    

#=====================
#Função de Listar Despesas
#=====================

def listar():

    while True:
        limpar_tela()

        titulo("LISTAR DESPESAS")

        lista()

        print("\n================================")
        print("1. Voltar")
        print("2. Sair")
        print("=================================\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu()
            return True
        elif opcao == "2":
            sair()
            return True
        else:
            aviso("INSIRA UM VALOR VÁLIDO!!!")


#=====================
#Função de Listar
#=====================

def editar():

    while True:
        limpar_tela()
    
        titulo("EDITAR DESPESAS")
    
        lista()
    
        print("\n================================")
        print("1. Editar")
        print("2. Voltar")
        print("3. Sair")
        print("=================================\n")
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":
            limpar_tela()

            titulo("EDITAR")

            id_buscar = int(input("Digite o ID da despesa: "))

            with open(caminho, "r", encoding="utf=8") as arquivo:
                despesas = json.load(arquivo)

            for item in despesas:
                if item['ID'] == id_buscar:
                    item['Nome'] = input(f"Novo nome (atual: {item['Nome']}): ") or item['Nome']
                    item['Valor'] = input(f"Novo valor (atual: {item['Valor']}R$): ") or item['Valor']
                    item['Categoria'] = input(f"Novo categoria (atual: {item['Categoria']}): ") or item['Categoria']
                    item['Data'] = input(f"Novo data (atual: {item['Data']}): ") or item['Data']
                    break
            else:
                aviso("DESPESA NÃO ENCONTRADA!!!")

            with open(caminho, "w", encoding="utf=8") as arquivo:
                json.dump(despesas, arquivo, indent=4, ensure_ascii=False)

        elif opcao == "2":
            menu()
            return True
        elif opcao == "3":
            sair()
            return True
        else:
            aviso("INSIRA UM VALOR VÁLIDO!!!")

#=====================
#Função de Excluir
#=====================

def excluir():

    while True:
        limpar_tela()
    
        titulo("EXCLUIR DESPESAS")
    
        lista()
    
        print("\n================================")
        print("1. Excluir")
        print("2. Voltar")
        print("3. Sair")
        print("=================================\n")
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":
            limpar_tela()

            titulo("EXCLUIR")

            excluir_id = int(input("Digite o ID da despesa: "))

            with open(caminho, "r", encoding="utf=8") as arquivo:
                despesas = json.load(arquivo)

            despesas = [
                despesa for despesa in despesas
                if despesa["ID"] != excluir_id
            ]

            with open(caminho, "w", encoding="utf=8") as arquivo:
                json.dump(despesas, arquivo, indent=4, ensure_ascii=False)

            aviso("DESPESA EXCLUÍDA")

        elif opcao == "2":
            menu()
            return True
        elif opcao == "3":
            sair()
            return True
        else:
            aviso("INSIRA UM VALOR VÁLIDO!!!")
            
#=====================
#Função de Visualizar Gastos por Categoria
#=====================

def ver_gastos():

    while True:
        limpar_tela()

        existe = False

        with open(caminho, "r", encoding="utf=8") as arquivo:
            despesas = json.load(arquivo)

        titulo("VISUALIZAR GASTOS")

        print("\n================================")
        print("1. Pesquisar")
        print("2. Voltar")
        print("3. Sair")
        print("=================================\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()

            titulo("CATEGORIA")

            categoria = input("Digite a categoria: ")

            print("\n================================\n")

            for item in despesas:
                if categoria == item['Categoria']:
                    print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']}R$ | Categoria: {item['Categoria']}")
                    existe = True

            if existe == False:
                print("Nenhuma despesa encontrada nessa categoria!!!")

            print("\n================================\n")
            input("Pressione ENTER para continuar...")

        elif opcao == "2":
            menu()
            return True
        elif opcao == "3":
            sair()
            return True
        else:
            aviso("INSIRA UM VALOR VÁLIDO!!!")

#=====================
#Função de Visualizar Gastos
#=====================

def ver_total():

    limpar_tela()

    titulo("VISUALIZAR TOTAL")

    lista()

    with open(caminho, "r", encoding="utf=8") as arquivo:
        despesas = json.load(arquivo)

    total = 0

    for item in despesas:
        total += float(item['Valor'].replace(',', '.'))

    print("\n================================\n")
    print(f"Total: {total:.2f}R$")
    print("\n================================")
    print("1. Voltar")
    print("2. Sair")
    print("=================================\n")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        menu()
        return True
    elif opcao == "2":
        sair()
        return True
    else:
                aviso("INSIRA UM VALOR VÁLIDO!!!")

def sair():

    limpar_tela()
    print("\n================================")
    print("Sistema encerrado!!!")
    print("================================\n")


def escolhas(opcao):

    match opcao:
        case "1":
            cadastrar()
        case "2":
            listar()
        case "3":
            editar()
        case "4":
            excluir()
        case "5":
            ver_gastos()
        case "6":
            ver_total()
        case "7":
            sair()
menu()