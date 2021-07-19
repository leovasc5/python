class Pessoa:
    def __init__(self, nome, idade, velocidade):
        self.nome = self.setNome(nome)
        self.idade = self.setIdade(idade)
        self.velocidade = self.setVelocidade(velocidade)
        self.corridos = 0
        
    def setNome(self, nome):
        self.nome = nome
        print(f'{self.nome} está vivo e jogará no vasco')

    def setIdade(self, idade):
        self.idade = idade