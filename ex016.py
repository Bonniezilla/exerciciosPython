metrosQuadrados = float(input('Quantos metros quadrados tem a área: '))

lataValor = 80
lataLitros = 18
litroMetros = 3

calculoLitros = metrosQuadrados / litroMetros
quantidadeLatas = round(calculoLitros / lataLitros)
precoTotal = quantidadeLatas * lataValor

print("Serão necessárias" , quantidadeLatas , "latas")
print("O preço total é de R$" , precoTotal)

