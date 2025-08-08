import os
import json

# Arquivos de dados
ARQ_PRODUTOS = "produtos.json"
ARQ_CLIENTES = "clientes.json"
ARQ_PEDIDOS = "pedidos.json"

# Carregamento dos dados do sistema
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Dados em memória
produtos = carregar_dados(ARQ_PRODUTOS)
clientes = carregar_dados(ARQ_CLIENTES)
pedidos = carregar_dados(ARQ_PEDIDOS)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções principais
def cadastrar_produto():
    limpar_tela()
    print("=== CADASTRO DE PRODUTO ===")
    nome = input("Nome do produto: ")
    preco = float(input("Preço (R$): "))
    ingredientes = input("Ingredientes: ")
    produto = {
        'nome': nome,
        'preco': preco,
        'ingredientes': ingredientes.split(",")
    }
    produtos.append(produto)
    salvar_dados(ARQ_PRODUTOS, produtos)
    print(f"\nProduto '{nome}' cadastrado com sucesso!")
    input("Pressione ENTER para continuar...")

def visualizar_cardapio():
    limpar_tela()
    print("=== CARDÁPIO ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(produtos, 1):
            print(f"{i}. {produto['nome']} - R$ {produto['preco']:.2f}")
            print(f"   Ingredientes: {', '.join(produto['ingredientes'])}")
    input("\nPressione ENTER para voltar ao menu...")

def cadastrar_cliente():
    limpar_tela()
    print("=== CADASTRO DE CLIENTE ===")
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    numero = input("numero: ")
    email = input("Email: ")
    cliente = {
        'nome': nome,
        'cpf': cpf,
        'numero': numero,
        'email': email
    }
    clientes.append(cliente)
    salvar_dados(ARQ_CLIENTES, clientes)
    print(f"\nCliente '{nome}' cadastrado com sucesso!")
    input("Pressione ENTER para continuar...")

def realizar_pedido():
    limpar_tela()
    if not clientes or not produtos:
        print("Clientes ou produtos não cadastrados. Cadastre-os antes de continuar.")
        input("Pressione ENTER para voltar...")
        return

    print("=== REALIZAR PEDIDO ===")
    print("\nClientes:")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente['nome']} ({cliente['email']}) ({cliente['cpf']})")
    cliente_id = int(input("Selecione o cliente pelo número: ")) - 1

    print("\nCardápio:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto['nome']} - R$ {produto['preco']:.2f}")
    pedido_ids = input("Digite os números dos produtos: ").split(",")

    total = 0
    itens = []
    for pid in pedido_ids:
        produto = produtos[int(pid.strip()) - 1]
        itens.append(produto)
        total += produto['preco']

    pedido = {
        'cliente': clientes[cliente_id],
        'itens': itens,
        'total': total
    }
    pedidos.append(pedido)
    salvar_dados(ARQ_PEDIDOS, pedidos)
    print(f"\nPedido realizado com sucesso! Total a Pagar: R$ {total:.2f}")
    input("Pressione ENTER para continuar...")

def relatorio_vendas():
    limpar_tela()
    print("=== RELATÓRIO DE VENDAS ===")
    if not pedidos:
        print("Nenhum pedido registrado ainda.")
    else:
        total_dia = sum(p['total'] for p in pedidos)
        print(f"Total de vendas do dia: R$ {total_dia:.2f}")
        print(f"Número de pedidos: {len(pedidos)}")
    input("\nPressione ENTER para continuar...")

def menu():
    while True:
        limpar_tela()
        print("==== COFFEE SHOPS TIA ROSA ====")
        print("1. Cadastrar Produto")
        print("2. Visualizar Cardápio")
        print("3. Cadastrar Cliente")
        print("4. Realizar Pedido")
        print("5. Relatório de Vendas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            visualizar_cardapio()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            realizar_pedido()
        elif opcao == "5":
            relatorio_vendas()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione ENTER para continuar...")

# Início do programa
if __name__ == "__main__":
    menu()