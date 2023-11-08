# Listas
clientes = []
estoque = []

# Funções
def menu():
    print('MENU DE OPCOES\n'
          '1 - Vender\n'
          '2 - Estoque\n'
          '3 - Cadastrar Cliente\n'
          '4 - Cadastrar Produto\n'
          '5 - Sair')

def vender():
    nome = input("nome")
    cliente = None

    for j in clientes:
         if j ["nome"] == nome:
            cliente = j

    if cliente:
        print(f"{cliente['nome']}{cliente['endereço']}{cliente['imail']}")
    else:
        print("cliente nao cadastrado : ")

    for i, produto in enumerate(estoque[:10]):
        print(f"{i} - {produto['nome']} - {produto['preco']}") 

    escolha = int(input("Digite sua escolha: "))
    produto_escolhido = estoque[escolha]   

    qtd = int(input("Digite a quantidade: "))

    if qtd <= produto_escolhido['quantidade']:
        produto_escolhido['quantidade'] -= qtd
    else:
        print("Estoque insuficiente")

    total = produto_escolhido['preco'] * qtd

    print(total)
    
             

def cadastrar_produto():
    # nome, código, preço e quantidade
    nome = input("Nome: ")
    codigo = input("Codigo: ")
    preco = float(input("Preco: "))
    qtd = int(input("Quantidade: "))

    produto = {
        'nome': nome,
        'codigo': codigo,
        'preco': preco,
        'quantidade': qtd
    }

    estoque.append(produto)
    print('Produto adicionado com sucesso!')

def cadastrar_cliente():
    nome = input("digite o nome :")
    endereço = input("endereço : ")
    email = input("imail") 
    telefone = input("telefone : ")

    cliente = {
        'nome': nome,
        'endereço': endereço,
        'imail': email,
        'telefone': telefone
}
    clientes.append(cliente)

    print("cadastrado com sucesso !")

def exibir_estoque():
        for dicionario in estoque:
             print(f"Nome: {dicionario['nome']}\n Codigo: {dicionario['codigo']}\n {dicionario['quantidade']}\n{dicionario['preco']}")


while True:
    menu()
    opcao = int(input("digite a opçao : "))

    match opcao:
            case 1:
                vender()
        
            case 2:
              exibir_estoque()

            case 3:
              cadastrar_cliente()

            case 4:
              cadastrar_produto()
            
            case 5:
                break
                
            case _:
                print("opçao invalida")