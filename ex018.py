arquivoMb = float(input("Quantos Mbs tem o arquivo? "))
velocidadeMb = float(input("Qual a velocidade do download em Mbps? "))

tempoEstimado = ((arquivoMb / velocidadeMb) / 10)
print("O tempo estimado em minutos é de: " , tempoEstimado)