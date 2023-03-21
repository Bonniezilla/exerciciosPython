ganhoHora = float(input('Quanto você ganha por hora? '))
horasTrabalho = float(input('Quantas horas você trabalhou? '))

salarioBruto = ganhoHora * horasTrabalho
impostoRenda = salarioBruto * (11/100)
impostoInss = salarioBruto * (8/100)
impostoSindicato = salarioBruto * (5/100)

salarioLiquido = salarioBruto - impostoRenda - impostoInss - impostoSindicato

print("O salário bruto é de: R$" , salarioBruto)
print('Devem ser pagos de imposto de renda: R$', impostoRenda)
print('Devem ser pagos de INSS: R$' , impostoInss)
print('Devem ser pagos ao Sindicato: R$' , impostoSindicato)
print('O salario líquido é de: R$' , salarioLiquido)

