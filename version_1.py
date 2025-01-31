from time import sleep

class humano:
    def __init__(self, life, armor, resist):
        self.life = life
        self.armor = armor
        self.resist = resist

    def life(self):
        return self.life
    def armor(self):
        return self.armor
    def resist(self):
        return self.resist

class mago(humano):
    def __init__(self, mana, knowledge):
        self.mana = mana
        self.knowledge = knowledge

class ork(humano):
    def __init__(self, fury, strength):
        self.fury = fury
        self.strength = strength



def creat_caracter(raca, classe):
    print ("criando personagem")
    sleep(2)
    print ("personagem criado")
    

def combate(player1, player2):
    pass



persona_1 = creat_caracter(humano(100, 50, 70), mago(70, 30))
persona_2 = creat_caracter(humano(100, 50, 70), ork(50, 20))


print (persona_1)

