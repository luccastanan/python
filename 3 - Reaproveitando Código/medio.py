# Pesquisa com uma quantidade x de pessoas, 
# se essa pessoa tiver 17 anos ou mais e 26 anos ou menos, será solicitado seu curso

def formulario(numPessoa):
	print('Pessoa {}'.format(numPessoa))
	nome = input('Seu nome: ')
	idade = int(input('Sua idade: '))
	return (nome, idade)

def formacao():
	curso = input('Seu curso: ')
	ano = int(input('Ano que está: '))
	return (curso, ano)

def inicio():
	numero = int(input('Numero de pessoas que vão participar da pesquisa: '))
	return numero

quantidadePessoas = inicio()
pessoas = []
for numPessoa in range(quantidadePessoas):
	pessoa = formulario(numPessoa + 1)
	pessoas.append(pessoa)
	if(pessoa[1] >= 17 and pessoa[1] <= 26):
		form = formacao()
		pessoas.append(form)
print(pessoas)