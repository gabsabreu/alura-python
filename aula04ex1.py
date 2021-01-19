print('***************************************')
print('Bem vinda(o) ao jogo de adivinhação!')
print('***************************************')

num_secreto = 63
qtd_tentativas = 3
rodada = 1

while(rodada <= qtd_tentativas):
    print('Tentativa {} de {}'.format(rodada,qtd_tentativas))
    chute = int(input('Digite o seu chute: '))
    if (num_secreto == chute):
        print('Você acertou!')
    else:
        if (chute > num_secreto):
            print('Você errou! O seu chute foi maior que o número secreto.')
        else:
            print('Você errou! O seu chute foi menor que o número secreto.')
    rodada = rodada + 1
print('Fim do jogo')
