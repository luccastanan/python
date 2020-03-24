idade = int(input('Sua idade: '))
peso = float(input('Seu peso: '))

# é maior de idade?
if(idade >= 18):
    print('É maior de idade')
else:
    print('É menor de idade')

if(idade >= 22 and peso >= 70):
    print('Pode servir do exercito')