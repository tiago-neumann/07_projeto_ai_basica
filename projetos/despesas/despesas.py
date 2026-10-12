import json
from datetime import datetime
import time
import os

data = datetime.now().strftime("%d/%m/%y")
erro = True

#=====================
#Função de Limpar a Tela
#=====================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#=====================
#Função de Exibir Menu
#=====================

def menu():

    limpar_tela()

    while True:
        print("\n================================")
        print("GERENCIADOR DE DESPESAS")
        print("================================\n")
        print("1. Cadastrar despesa") 
        print("2. Listar despesas")
        print("3. Editar despesa")
        print("4. Excluir despesa")
        print("5. Ver gastos por categoria")
        print("6. Ver total do mês")
        print("7. Definir orçamento mensal")
        print("8. Salvar e sair")
        print("\n================================\n")

        opcao = input("Escolha uma opção: ")

        limpar_tela()

        if opcao not in ["1", "2", "3", "4", "5", "6", "7", "8"]:  
            print("\nInsira um valor válido!")
            time.sleep(1)
            limpar_tela()
        else:
            escolhas(opcao)
            return True

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta_atual, "despesas.json")

#=====================
#Função de Cadastrar Despesas
#=====================

def cadastrar():

    print("\n================================")
    print("CADASTRAR DESPESAS")
    print("================================\n")

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

    limpar_tela()

    print("DESPESA CADASTRADA!!!")   
    time.sleep(1)

    menu()    

#=====================
#Função de Listar Despesas
#=====================

def listar():

    while True:
        limpar_tela()

        with open(caminho, "r", encoding="utf=8") as arquivo:
            despesas = json.load(arquivo)

        print("\n================================")
        print("LISTAR DESPESAS")
        print("================================\n")

        for item in despesas:
            print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']} | Categoria: {item['Categoria']}")

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
            limpar_tela()
            print("\nInsira um valor válido!")
            time.sleep(1)


#=====================
#Função de Listar
#=====================

def editar():

    while True:
        limpar_tela()
    
        with open(caminho, "r", encoding="utf=8") as arquivo:
            despesas = json.load(arquivo)
    
        print("\n================================")
        print("EDITAR DESPESAS")
        print("================================\n")
    
        for item in despesas:
            print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']} | Categoria: {item['Categoria']}")
    
        print("\n================================")
        print("1. Editar")
        print("2. Voltar")
        print("3. Sair")
        print("=================================\n")
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":

            print("\n================================")
            print("EDITAR")
            print("=================================\n")

            id_buscar = int(input("Digite o ID da despesa: "))

            for item in despesas:
                if item['ID'] == id_buscar:
                    item['Nome'] = input(f"Novo nome (atual: {item['Nome']}): ") or item['Nome']
                    item['Valor'] = input(f"Novo valor (atual: {item['Valor']}): ") or item['Valor']
                    item['Categoria'] = input(f"Novo categoria (atual: {item['Categoria']}): ") or item['Categoria']
                    item['Data'] = input(f"Novo data (atual: {item['Data']}): ") or item['Data']
                    break
            else:
                print("ID não encontrado!!!")
                time.sleep(1)

            with open(caminho, "w", encoding="utf=8") as arquivo:
                json.dump(despesas, arquivo, indent=4, ensure_ascii=False)

        elif opcao == "2":
            menu()
            return True
        elif opcao == "3":
            sair()
            return True
        else:
            limpar_tela()
            print("\nInsira um valor válido!")
            time.sleep(1)

#=====================
#Função de Excluir
#=====================

def excluir():

    while True:
        limpar_tela()
    
        with open(caminho, "r", encoding="utf=8") as arquivo:
            despesas = json.load(arquivo)
    
        print("\n================================")
        print("EXCLUIR DESPESAS")
        print("================================\n")
    
        for item in despesas:
            print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']} | Categoria: {item['Categoria']}")
    
        print("\n================================")
        print("1. Excluir")
        print("2. Voltar")
        print("3. Sair")
        print("=================================\n")
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":

            print("\n================================")
            print("EXCLUIR")
            print("================================\n")

            excluir_id = int(input("Digite o ID da despesa: "))

            despesas = [
                despesa for despesa in despesas
                if despesa["ID"] != excluir_id
            ]

            with open(caminho, "w", encoding="utf=8") as arquivo:
                json.dump(despesas, arquivo, indent=4, ensure_ascii=False)

            limpar_tela()
            print("Despesa excluída com sucesso!")
            time.sleep(1)

        elif opcao == "2":
            menu()
            return True
        elif opcao == "3":
            sair()
            return True
        else:
            limpar_tela()
            print("\nInsira um valor válido!")
            
#=====================
#Função de Visualizar Gastos por Categoria
#=====================

def ver_gastos():

    print("\n================================")
    print("VISUALIZAR GASTOS")
    print("================================\n")

    categoria = input("Escolha uma categoria para verificar os gastos: ")

    with open(caminho, "r", encoding="utf=8") as arquivo:
        despesas = json.load(arquivo)

    print("\n================================")

    for item in despesas:
        if categoria == item['Categoria']:
            print(f"ID: {item['ID']} | Data: {item['Data']} | Nome: {item['Nome']} | Valor: {item['Valor']} | Categoria: {item['Categoria']}")
        else:
            print("Nenhuma despesa encontrada nessa categoria!!!")

    print("================================")


#def ver_total():


#def orcamento():


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
        case "8":
            sair()
menu()