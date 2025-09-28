class Arachnids:
    def __init__(self, species, description, venom, lethal):
        self.species = species 
        self.description = description, 
        self.venom = venom
        self.lethal = lethal
        
    def is_spiders(self, species):
        is_spider = False
        # TO DO: implement later 
        spider_species = ["Tarantula", "Black Widow", "Jumping Spider", "common spider"]
        for spider in range(len(spider_species)):
            if self.species == spider:
                return True
        return False 
    