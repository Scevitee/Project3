class Pakuri:
    def __init__(self, species):
        self.species = species #okay to use species here, everywhere else use self.species
        self.attack = (len(species) * 7) + 9
        self.defense =  (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # getter: retrieve the attribute value
    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    # setter: update the attribute's value
    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        pass




pakuri = Pakuri("Pikabu")