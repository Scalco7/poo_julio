class Programa(object):
    def __init__(self):
        self.bob = Cachorro("bob", 3, 40, 10, 60)

        self.bob.latir()
        self.bob.dormir()
        self.bob.comer()
 

class Cachorro(object):
    
    def __init__(self, nome, idade, saude, afeto, fome):
        self.nome = nome
        self.idade = idade
        self.saude = saude
        self.afeto = afeto
        self.fome = fome

    def latir(self):
        print("Au au")

    def comer(self):
        self.afeto += 10
        self.fome += 10
        
        if self.afeto > 100:
            self.afeto = 100
        
        if self.fome > 100:
            self.fome = 100

        print(f"A fome esta em {self.fome}")
        print(f"O efeto esta em {self.afeto}")
        
    
    def dormir(self):
        self.saude += 10
        
        if self.saude > 100:
            self.saude = 100
        
        print(f"A saude é {self.saude}")

Programa()
        
