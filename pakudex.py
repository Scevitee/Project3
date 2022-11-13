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
        for item in self.pakuri_list:
            if item.species == pakuri.get_species():
                stat_ls.extend([pakuri.get_species(), pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()])
                return stat_ls
        return None




    def sort_pakuri(self):
        # approach 2 (from prior notes)
        # or use approach 1 -> create separate __lt__ for comparison
        self.pakuri_list.sort(key=lambda paku: paku.name)

    def add_pakuri(self, species):
        pakuri = Pakuri(species)
        ##### Check if I need to do this for some of the other functions above as well
        #### Note: I don't think that I do.
        # add this pakuri into self.pakuri_list (in the __init__ def)
        # increment self.size by 1
        # 1. Check duplicates
        # 2. check if list is full
        if pakuri not in self.pakuri_list:
            # This may need to be comparing the species name
            # Something like pakuri.species not in self.pakuri_list
            if self.size < self.capacity:
                self.pakuri_list.append(pakuri)
        return self.pakuri_list


    def evolve_species(self, species):
        # Attempts to evolve species within pakudex.
        # If unsuccessful, return True, return False otherwise
        ## Why wouldn't it be able to evolve a species??
        ### Inputted species doesn't exist
        if species in self.pakuri_list:
            species.evolve()
            return False
        else:
            return True




