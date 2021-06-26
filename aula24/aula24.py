class Jogador:

    def __init__(self, nome, equipe, nacionalidade, overall):
        self.nome = nome
        self.equipe = equipe
        self.nacionalidade = nacionalidade
        self.overall = overall
    
    def getDados(self):
        array = []
        array.append(self.nome)
        array.append(self.equipe)
        array.append(self.nacionalidade)
        array.append(self.overall)
        return array

class Aposentado(Jogador):
    def __init__(self, nome, nacionalidade, overall):
        self.equipe = "Old Boys"
        super().__init__(nome, self.equipe, nacionalidade, overall)
    
class Juvenil(Jogador):
    def __init__(self, nome, nacionalidade, overall):
        self.equipe = "Base"
        super().__init__(nome, self.equipe, nacionalidade, overall)

j1 = Juvenil("Menino", "Brasileiro", 74)
print(j1.getDados())

j2 = Aposentado("Zé Roberto", "Brasileiro", 89)
print(j2.getDados())