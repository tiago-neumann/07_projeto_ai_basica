"""repeticao - Ele vai criar a variável 'repeticao' e vai chamar um input pra receber um valor"""
"""caracter - Ele vai criar a variável 'caracter' e vai chamar um input pra receber o caracter"""

repeticao = int(input("Digite o numero de repetições: "))
caracter = input("Digite o carácter que será utilizado: ")

"""for - Ele cria um for que se repete o numero de vezes do dado posto no input de repeticao"""

for i in range(repeticao):

    """espaco - Ele cria a variável 'espaco', que pega o numero de repetições, diminui o valor de 'i' e menos 1"""
    """quantidade - Ele cria a variável 'quantidade', que múltiplica o 'i' e soma mais 1, assim sempre ficando ímpar"""
    """print - Ele só faz os dados aparecerem na tela, múltiplicando o 'espaco' por espaços vazios e o 'caracter' pelo numero de 'quantidade'"""

    espaco = repeticao - i - 1
    quantidade = 2 * i + 1
    print(espaco * " " + caracter * quantidade)