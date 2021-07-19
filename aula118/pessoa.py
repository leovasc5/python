class Pessoa:
    def __init__(self, nome, idade, velocidade, comendo=False, falando=False):
        self.nome = self.setNome(nome)
        self.idade = self.setIdade(idade)
        self.velocidade = self.setVelocidade(velocidade)
        self.corridos = 0
        
    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

   
    