import random

vidas = int(input("Informe O numero de vidas: "))
while vidas <= 0:
     vidas=int(input('Você digitou um numero de vidas inválido. Tente Novamente.\n'))
qtd = int(input("Digite a quantidade de palavras: "))

while qtd <= 0:
    qtd=int(input('Você digitou uma quantidade de palavras inválida. Tente Novamente.\n'))

listaPalavras = list()
i = 1
while i <= qtd:
        palavra = str(input(f"Digite a {i} º palavra:  ")).upper()
        listaPalavras.append(palavra)#adiciona as palavras na lista de palavras.
        i += 1

continuacao = 'sim'
while continuacao == 'sim':
     
     palAleatoria = random.choice(listaPalavras)#sorteia e armazena uma das palavras da lista.
     palDescrypt = list() 
     palCrypt = list()

     for i in palAleatoria: #transforma a palavra aleatoria em uma lista de letras dentro da variavel palDescrypt
        palDescrypt.append(i)    
     tam = len(palAleatoria)     
