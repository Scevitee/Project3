from pakuri import *

class Pakudex:
    # Pakudex has a list of pakuri
    def __init__(self, capacity=20):
        self.pakuris = []
        self.capacity = capacity
        self.size = 0

    def get_size(self):
        self.size = len(self.pakuris)
        return self.size



    def sort_pakuri(self):
        # approach 2 (from prior notes)
        # or use approach 1 -> create separate __lt__ for comparison





    def add_pakuri(self, species):
        pakuri = Pakuri(species)
        # add this pakuri into self.pakuris (in the __init__ def)
        # increment self.size by 1
        # 1. Check duplicates
        if species in self.get_species_array():
            pass
        # 2. check if list is full
        pass

    def get_species_array(self):
        # iterate though self.pakuris
        # self.pakuris = [p1, p2, p3, p4, p4 ...]
        # for each pakuri in self.pakuris:
            # sp = get species of pakuri
            # append sp to final results list
        pass