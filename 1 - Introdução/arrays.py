idades = [5, 10, 6, 15, 19, 80, 50, 30, 2]

#idades mas quero acessar a posição onde está o número 10
print(idades[1])

#exibir idades menores de 50
for idade in idades:
    if idade <=  50:
        print(idade)

#quantas idades são maiores ou iguais 15
contador = 0
for idade in idades:
    if idade >= 15:
        contador = contador + 1
print('Quantidade de idades maiores ou iguais a 15: ' + str(contador))