from produto import Produto           
  #IMPORTAÇÃO DO PRODUTO.PY PRO MENU.PY
produtos = []

def adicionar_produto():
    #FUNÇÃO PARA ADICIONAR PRODUTOS

    nome = input("Nome do produto: ")                                       
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    novo_produto = Produto(nome, preco, quantidade)
    produtos.append(novo_produto)
    print("Produto adicionado com sucesso!")
    #ASSIM QUE ADICONAR O  PRODUTO

def exibir_produtos():
    #FUNÇÃO DE EXIBIR OS PRODUTOS

    if not produtos:
        print("Nenhum produto cadastrado.")
        #CASO NÃO TENHA NENHUM PRODUTO REGISTRADO
        return
    print("Produtos cadastrados:")
    for produto in produtos:
        produto.exibir_informacoes()
        print("-" * 20)

def atualizar_preco():
     #FUNÇÃO PARA ATUALIZAR O PREÇO DOS PRODUTOS

    nome = input("Nome do produto a atualizar o preço: ")
    for produto in produtos:
        if produto.nome == nome:
            novo_preco = float(input("Novo preço: "))
            produto.atualizar_preco(novo_preco)
            return
    print("Produto não encontrado.")
    

def atualizar_quantidade():
    #FUNÇÃO PARA ATUALIZAR A QUANTIDADE DE PRODUTOS
    nome = input("Nome do produto a atualizar a quantidade: ")
    for produto in produtos:
        if produto.nome == nome:
            nova_quantidade = int(input("Nova quantidade: "))
            produto.atualizar_quantidade(nova_quantidade)
            return
    print("Produto não encontrado.")
    #CASO NÃO TENHA NENHUM

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Exibir Produtos")
        print("3. Atualizar Preço")
        print("4. Atualizar Quantidade")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            exibir_produtos()
        elif opcao == '3':
            atualizar_preco()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()