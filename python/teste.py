# --- Loja Simples ---

# Dicionários para armazenar dados
estoque = {}
vendas = []

# --- Funções do sistema ---

def cadastrar_produto():
    nome = input("Nome do produto: ").capitalize()
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))
    estoque[nome] = {'preço': preco, 'quantidade': quantidade}
    print(f"✅ Produto '{nome}' cadastrado com sucesso!\n")

def listar_produtos():
    if not estoque:
        print("📦 Nenhum produto cadastrado.\n")
        return
    print("\n--- Estoque Atual ---")
    for nome, info in estoque.items():
        print(f"{nome}: R${info['preço']:.2f} | {info['quantidade']} unidades")
    print()

def vender_produto():
    nome = input("Nome do produto vendido: ").capitalize()
    if nome not in estoque:
        print("❌ Produto não encontrado!\n")
        return
    qtd = int(input("Quantidade vendida: "))
    if qtd > estoque[nome]['quantidade']:
        print("⚠️ Estoque insuficiente!\n")
        return
    estoque[nome]['quantidade'] -= qtd
    total = qtd * estoque[nome]['preço']
    vendas.append({'produto': nome, 'quantidade': qtd, 'total': total})
    print(f"💰 Venda registrada! Total: R${total:.2f}\n")

def relatorio_vendas():
    if not vendas:
        print("📊 Nenhuma venda registrada ainda.\n")
        return
    total_geral = sum(v['total'] for v in vendas)
    print("\n--- Relatório de Vendas ---")
    for v in vendas:
        print(f"{v['produto']} - {v['quantidade']} un - R${v['total']:.2f}")
    print(f"\n💵 Total arrecadado: R${total_geral:.2f}\n")

# --- Menu Principal ---
while True:
    print("=== MENU LOJA ===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Vender Produto")
    print("4. Relatório de Vendas")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        vender_produto()
    elif opcao == "4":
        relatorio_vendas()
    elif opcao == "5":
        print("👋 Encerrando o sistema. Até mais!")
        break
    else:
        print("❌ Opção inválida!\n")

