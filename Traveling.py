class Traveling:
    def __init__(self, sightseeing, noob, event, experienced, music, attraction):
        self.sightseeing = sightseeing
        self.noob = noob
        self.event = event
        self.experienced = experienced
        self.music = music
        self.attraction = attraction
    
    def tourists(self, sightseeing):
        if sightseeing:
            return("Go see " + self.attraction)
        elif sightseeing and self.noob: 
            return(" You need to learn of " + self.event)
        else:
            return("Go home!")
    