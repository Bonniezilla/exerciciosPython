import math
metrosQuadrados = float(input('Quantos metros quadrados tem a área: '))

quantidadeGaloes = 0
quantidadeLatas = 0

litroMetros = 6

lataValor = 80
lataLitros = 18
galaoValor = 25
galaoLitros = 3.6


calculoLitros = metrosQuadrados / litroMetros

quantidadeLatas = math.ceil(calculoLitros / lataLitros)
quantidadeGaloes = math.ceil(calculoLitros / galaoLitros)

precoTotalLatas = quantidadeLatas * lataValor
precoTotalGaloes = quantidadeGaloes * galaoValor

print("Serão necessárias" , quantidadeLatas , "latas")
print("Serão necessárias" , quantidadeGaloes , "galoes")

print('Preco total em latas R$' , precoTotalLatas)
print('Preco total em galões R$' , precoTotalGaloes)

