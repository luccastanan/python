valores = []
#range(5) == [0, 1, 2, 3, 4]
for count in range(5):
	valor = int(input('Digite o valor {}: '.format(count+1)))
	valores.append(valor)
print(valores)