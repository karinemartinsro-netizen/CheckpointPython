import random
print("Vamos jogar um jogo de adivinhação ? ")
numero_sorteado = random.randint(1, 101)


while True:
    numero_digitado = int (input("Escolha um número de 1 á 100   "))

    if (numero_digitado == numero_sorteado):
        print(f"Acertou , o número sorteado pelo sistema foi : - {numero_sorteado}  ")
        print("Parabéns !!!")
        break

    elif (numero_digitado < numero_sorteado):
        print(f"Você errou , o número sorteado pelo sistema á maior que {numero_digitado}")
    else:
        print(f"O número sorteado é MENOR que {numero_digitado}")

# print(f"{numero_sorteado}")