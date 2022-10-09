from ast import With
import json
from os.path import exists


ARQ_CARROS = "carros.json"
ARQ_VENDEDORES = "vendedores.json"
ARQ_CLIENTES = "clientes.json"


def cadastrar_carro():
    cadastro_carro = {
        "Nome": "",
        "Cor": "",
        "Placa": "",
        "Vendido": False,  # inicia como não vendido por padrão
    }

    # cria o arquivo se ele não existir
    if not exists(ARQ_CARROS):
        with open(ARQ_CARROS, "w") as f:
            json.dump({}, f, indent=4)

    # carrega o arquivo
    with open(ARQ_CARROS, "r") as f:
        dicionario_saida = json.load(f)
        carros_json = json.load(f)

        # código pra não deixar um carro ser cadastrado com um id já utilizado
        aux = True
        while aux:
            id_cadastro = input("Digite o id do carro a ser cadastrado: ")
            if id_cadastro in carros_json:
                print("Já existe um carro com esse id, tente novamente.")
            else:
                aux = False

        print("Digite os dados a seguir")
        cadastro_carro["Nome"] = input("Digite o nome do carro: ")
        cadastro_carro["Cor"] = input("Digite a cor do carro: ")
        cadastro_carro["Placa"] = input("Digite a placa do carro: ")

    # escreve o que já tava no arquivo e adiciona o novo carro
    with open(ARQ_CARROS, "w") as f:
        dicionario_saida[id_cadastro] = cadastro_carro
        json.dump(dicionario_saida, f, indent=4)
    print()


def cadastrar_cliente():
    cadastro_cliente = {
        "Nome": "",
        "Telefone": "",
        "No de compras": 0,
    }

    # cria o arquivo se ele não existir
    if not exists(ARQ_CLIENTES):
        with open(ARQ_CLIENTES, "w") as f:
            json.dump({}, f, indent=4)

    # carrega o arquivo
    with open(ARQ_CLIENTES, "r") as f:
        dicionario_saida = json.load(f)
        clientes_json = json.load(f)

        # código pra não deixar um cliente ser cadastrado com um id já utilizado
        aux = True
        while aux:
            id_cadastro = input("Digite o id do cliente a ser cadastrado: ")
            if id_cadastro in clientes_json:
                print("Já existe um cliente com esse id, tente novamente.")
            else:
                aux = False

        print("Digite os dados a seguir")
        cadastro_cliente["Nome"] = input("Digite o nome do cliente: ")
        cadastro_cliente["Telefone"] = input("Digite o telefone do cliente: ")
        cadastro_cliente["Compras"] = []

    # escreve o que já tava no arquivo e adiciona o novo cliente
    with open(ARQ_CLIENTES, "w") as f:
        dicionario_saida[id_cadastro] = cadastro_cliente
        json.dump(dicionario_saida, f, indent=4)
    print()


def cadastrar_vendedor():
    cadastro_vendedor = {
        "Nome": "",
        "Telefone": "",
        "No de vendas": 0,
    }

    # cria o arquivo se ele não existir
    if not exists(ARQ_VENDEDORES):
        with open(ARQ_VENDEDORES, "w") as f:
            json.dump({}, f, indent=4)

    # carrega o arquivo
    with open(ARQ_VENDEDORES, "r") as f:
        dicionario_saida = json.load(f)
        vendedores_json = json.load(f)

        # código pra não deixar um vendedor ser cadastrado com um id já utilizado
        aux = True
        while aux:
            id_cadastro = input("Digite o id do vendedor a ser cadastrado: ")
            if id_cadastro in vendedores_json:
                print("Já existe um vendedor com esse id, tente novamente.")
            else:
                aux = False

        print("Digite os dados a seguir")
        cadastro_vendedor["Nome"] = input("Digite o nome do vendedor: ")
        cadastro_vendedor["Telefone"] = input("Digite o telefone do vendedor: ")
        cadastro_vendedor["Vendas"] = []

    # escreve o que já tava no arquivo e adiciona o novo vendedor
    with open(ARQ_VENDEDORES, "w") as f:
        dicionario_saida[id_cadastro] = cadastro_vendedor
        json.dump(dicionario_saida, f, indent=4)
    print()


def menu_cadastrar():
    print("=== MENU CADASTRAR ===")
    print("Digite o que você deseja cadastrar:")
    print("(1) Carro")
    print("(2) Cliente")
    print("(3) Vendedor")
    print("(0) Voltar")
    opcao = int(input("Digite sua opção: "))

    if opcao == 0:
        return
    elif opcao == 1:
        cadastrar_carro()
    elif opcao == 2:
        cadastrar_cliente()
    elif opcao == 3:
        cadastrar_vendedor()


def vender():
    if not exists(ARQ_CARROS):
        print("Não há carros disponíveis para a venda!")
        return

    # carrega o arquivo
    with open(ARQ_CARROS, "r") as f:
        carros_json = json.load(f)
        carros_disponiveis = {}

        # adiciona os carros nao vendidos no dicionario
        for id, carro in carros_json.items():
            if not carro["Vendido"]:
                carros_disponiveis[id] = carro

        if len(carros_disponiveis) < 1:
            print("Não há carros disponíveis para a venda!")
            return
        else:
            for id, carro in carros_disponiveis.items():
                print(f"ID do carro: {id}\nDetalhes:{carro}")
            id_carro = int(input("Digite o ID do carro desejado: "))
            id_cliente = int(input("Digite o ID do cliente: "))
            id_vendedor = int(input("Digite o ID do vendedor: "))

            carros_json[id_carro]["Vendido"] = {
                "Vendedor": id_vendedor,
                "Cliente": id_cliente,
            }

    with open(ARQ_CLIENTES, "r") as f:
        clientes_json = json.load(f)
        clientes_json[id_cliente]["Compras"].append(carros_json[id_carro])

    with open(ARQ_VENDEDORES, "r") as f:
        vendedores_json = json.load(f)
        vendedores_json[id_vendedor]["Vendas"].append(carros_json[id_carro])


def listar():
    print("=== MENU DE LISTAGEM ===")
    carros_vendidos = ""
    carros_nao_vendidos = ""

    # separa os carros vendidos dos não vendidos
    with open(ARQ_CARROS, "r") as f:
        carros_json = json.load(f)
        for carro in carros_json.values():
            if carro["Vendido"] == True:
                carros_vendidos += f"{carro}\n"
            else:
                carros_nao_vendidos += f"{carro}\n"

    print("Digite o que você quer ver:")
    print("(1) Carros vendidos")
    print("(2) Carros não vendidos")
    print("(3) Compras por cliente")
    print("(4) Vendas por vendedor")
    print("(0) Voltar")
    opcao = int(input("Digite sua opção: "))

    if opcao == 0:
        return
    elif opcao == 1:
        print(carros_vendidos)
    elif opcao == 2:
        print(carros_nao_vendidos)
    elif opcao == 3:
        with open(ARQ_CLIENTES, "r") as f:
            clientes_json = json.load(f)
            for cliente in clientes_json.values():
                print(f"Nome: {cliente['Nome']}\nCompras: {cliente['Compras']}\n")
    elif opcao == 4:
        with open(ARQ_VENDEDORES, "r") as f:
            vendedores_json = json.load(f)
            for vendedor in vendedores_json.values():
                print(f"Nome: {vendedor['Nome']}\nVendas: {vendedor['Vendas']}\n")

    print()


opcao = -1
while opcao != 0:
    print("=== MENU ===")
    print("(1) Cadastrar")
    print("(2) Vender")
    print("(3) Listar")
    print("(0) Sair")
    opcao = int(input("Digite sua opção: "))
    print()

    if opcao == 1:
        menu_cadastrar()
    elif opcao == 2:
        vender()
    elif opcao == 3:
        listar()
