import random
print("Vamos jogar um jogo de adivinhação ? ")
numero_sorteado = random.randint(1, 101)
tentativas = 0
tentativas_restantes = 7


while True:
    tentativas +=1

    numero_digitado = int (input("Escolha um número de 1 á 100   "))
    print(f"Tentativa {tentativas} de {tentativas_restantes}")
    if (numero_digitado == numero_sorteado):
        print(f"Acertou , o número sorteado pelo sistema foi : - {numero_sorteado}  ")
        print("Parabéns !!!")
        break
    elif (tentativas >= tentativas_restantes):
        print(f"Game over, suas chances terminaram , o número sorteado foi : -  {numero_sorteado}")
    elif (numero_digitado < numero_sorteado):
        print(f"Você errou , o número sorteado pelo sistema á maior que {numero_digitado}")
    else:
        print(f"O número sorteado é MENOR que {numero_digitado}")
