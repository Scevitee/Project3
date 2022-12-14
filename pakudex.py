from pakuri import *

class Pakudex:
    # Pakudex has a list of pakuri


    def __init__(self, capacity=20):
        self.pakuri_list = []
        self.capacity = capacity
        self.size = 0

    def get_size(self):
        self.size = len(self.pakuri_list)
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        # iterate though self.pakuris
        # self.pakuris = [p1, p2, p3, p4, p4 ...]
        # for each pakuri in self.pakuris:
            # sp = get species of pakuri
            # append sp to final results list
        species_arr = []
        for pak in self.pakuri_list:
            sp = pak.species
            species_arr.append(sp)
        return species_arr


    def get_stats(self, species):
        stat_ls = []
        pakuri = Pakuri(species)
        # compare the argument with the species names within the list
        # if they match, get the info from species in the list
        for item in self.pakuri_list:
            if item.species == pakuri.get_species():
                stat_ls.extend([item.get_species(), item.get_attack(), item.get_defense(), item.get_speed()])
                return stat_ls
        return None




    def sort_pakuri(self):
        # approach 2 (from prior notes)
        self.pakuri_list.sort(key=lambda paku: paku.species)

    def add_pakuri(self, species):
        pakuri = Pakuri(species)
        # add this pakuri into self.pakuri_list (in the __init__ def)
        # 1. Check duplicates
        # 2. check if list is full
        if pakuri not in self.pakuri_list:
            if self.size < self.capacity:
                self.pakuri_list.append(pakuri)
        return self.pakuri_list


    def evolve_species(self, species):
        # like in get_stats compare species names
        # iterate through and evolve the matched value within pakuri_list
        pakuri = Pakuri(species)
        i = 0
        for item in self.pakuri_list:
            if item.species == pakuri.get_species():
                self.pakuri_list[i].evolve()
                return True
            i += 1
        return False








