print()

print(' CALCULADORA DE CONSUMO DE GASOLINA ')
print()
print(' Criado por Henrique Wagner')
print(' Dia 12/09/2018')

print()

m = float(input(' Quanto seu carro faz por média?:  '))
d = float(input(' Qual será a distãncia que você irá percorrer?: '))
l = float(input(' Quanto está hoje em reais, o litro da gasolina?: '))


c = d/m

ct = c*l


print(' Você gastará {:.1f} reais ' .format(ct,))


print()

print()

input(' Digite qualquer coisa para sair ! ')