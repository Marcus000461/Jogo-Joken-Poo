import random
print(" Bem vindo ao jogo")
nome = input("Qual é o seu nome?")
idade = input("Qual é a sua idade?")
jogo =input("Você quer jogar um jogo s/n ?").lower()
# Se o jogador disser s o   jogo continua se ele disser n acaba o jogo
if jogo == "s":
    print("Prepare - se para jogar!")
# Opções possíveis
    opcoes = ['pedra', 'papel', 'tesoura']
# Escolha do usuário
    usuario = input('Escolha pedra, papel ou tesoura: ').lower()
#Escolha aleatória do computador
    computador = random.choice(opcoes)
    
    print(f" Você escolheu: {usuario}")
    print(f" O computador escolheu: {computador}")
# Conição de empate 
    if usuario == computador:
        print("empate")    
# Condição de vitoria do usuario
    elif (usuario =='pedra'and computador == ' tesoura') or \
         (usuario =='tesoura' and computador == 'papel')  or \
         (usuario == ' papel' and computador == 'pedra'):
             print( " Você venceu!")
    else:
        print(" Você perdeu!")
else:
    print("Ok, finalizando.")            
