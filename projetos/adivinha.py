"""import - Serve para importar bibliotecas"""

import random

"""aleatorio - Pego o 'random.randint(0, 100)' da biblioteca, fazendo ele dar um número aleatório a variável"""
"""tentativas - Vai guardar o número de vezes que você precisou tentar até chegar no número secreto"""

aleatorio = random.randint(0, 100)
tentativas = 0

print("!!!Adivinhe o número!!!")
print("Digite um número entre 0 a 100!")

"""while - Vai repetir a estrutura até que algo se torne verdade"""

while True:

    """palpite - Cria um input que deve ser inteiro"""
    """tentativas - Vai aumentando o número de tentativas conforme o jogo repete"""

    palpite = int(input())
    tentativas += 1

    """if, elif, else - Paramêtro de verificação que se algo acontece de acordo com sua regra ele executa algo diferente"""

    if palpite > aleatorio:
        print("Muito alto! Digite um número menor:")
    elif palpite < aleatorio:
        print("Muito baixo! Digite um número maior:")
    elif palpite < 0 or palpite > 100:
        print("Digite um número dentro dos parâmetros!!!")
    else:
        print("Parábens, você acertou o número!!!")
        print(f"Número secreto: {aleatorio}.")
        print(f"Tentativas: {tentativas}.")
