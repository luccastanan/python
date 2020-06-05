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