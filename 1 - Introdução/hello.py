class Pessoa:
    nome = ''
    idade = 0

    def __init__(self, parNome, parIdade):
        self.nome = parNome
        self.idade = parIdade
    
    def fazerAniversario(self):
        self.idade = self.idade + 1

pessoa = Pessoa('Luccas', 22)
pessoa2 = Pessoa('Marcos', 15)

print('{} tem {} anos'.format(pessoa.nome, pessoa.idade))
print('{} tem {} anos'.format(pessoa2.nome, pessoa2.idade))

pessoa.fazerAniversario()

print('{} agora tem {} anos'.format(pessoa.nome, pessoa.idade))
