# classe é a abstração de algo da realidade
# self é o contexto 
class Animal:
    
    def __init__(self, tipo, nome, som):
        self.tipo = tipo
        self.nome = nome
        self.som = som
    
    def produzirSom(self):
        return self.som

    def trocarNome(self, novoNome):
        self.nome = novoNome
#instância é a cópia de uma classe na memória do dispostivo
#objeto armazenada a instância de uma classe
#"meuAnimal" é o objeto
#"Animal('cachorro', 'bolinha', 'au au')" é a instância
meuAnimal = Animal('cachorro', 'bolinha', 'au au')
animalDoAmigo = Animal('gato', 'mimi', 'miau')
print(meuAnimal.nome)
print(meuAnimal.produzirSom())
print(animalDoAmigo.nome)
print(animalDoAmigo.produzirSom())

meuAnimal.trocarNome('morfeu')
print(meuAnimal.nome)