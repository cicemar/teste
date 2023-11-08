import random

def escolha_computador():
        escolhas = ['pedra', 'papel', 'tesoura']
        return random.choice(escolhas)

def verificar_vencedor(escolha_usuario, escolha_computador):
        if escolha_usuario == escolha_computador:
            return "Empate"
        elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or (escolha_usuario == 'tesoura' and escolha_computador == 'papel') or (escolha_usuario == 'papel' and escolha_computador == 'pedra'):
            return "Usuário venceu!"
        else:
            return "Computador venceu!"

def jogar():
        print("Bem-vindo ao jogo pedra, papel e tesoura!")
        print("Escolha uma opção: pedra, papel ou tesoura")
        escolha_usuario = input("Digite sua escolha: ")
        escolha_usuario = escolha_usuario.lower()
        

        if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Por favor, tente novamente.")
            return

        escolha_pc = escolha_computador()
        
        print("O computador escolheu:", escolha_pc)
        
        resultado = verificar_vencedor(escolha_usuario, escolha_pc)
        
        print(resultado)

while True:
    opcao = int(input("1 - Jogar;\n 2- Sair"))
    
    match opcao:
        case 1:
            jogar()
        case 2:
              break