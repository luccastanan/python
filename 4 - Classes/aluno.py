class Aluno:

    def __init__(self, nome, sobrenome, idade, curso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calc_media(self):
        return sum(self.notas) / len(self.notas)

aluno1 = Aluno('Luccas', "Galuppo Tanan", 22, 'Ciência da Computação')
aluno2 = Aluno('Bruno', 'Marcos', 27, 'Engenharia da Computação' )

aluno1.adicionar_nota(50)
aluno1.adicionar_nota(60)
aluno1.adicionar_nota(70)
aluno1.adicionar_nota(80)
print(aluno1.calc_media())