class Traveling:
    def __init__(self, sightseeing, noob, event, experienced, music, attraction, cost):
        self.sightseeing = sightseeing
        self.noob = noob
        self.event = event
        self.experienced = experienced
        self.music = music
        self.attraction = attraction
        self.cost = cost 
    
    def tourists(self, sightseeing):
        if sightseeing:
            return("Go see " + self.attraction)
        elif sightseeing and self.noob: 
            return(" You need to learn of " + self.event)
        else:
            return("Go home!")
    
    def calculate_total(self, cost_a, cost_b, cost_c):
        def helper_round_total(self, num):
            last_digit = num % 10
            if last_digit % 10 >= 5:
                return num + (10-last_digit)
            else:
                return num - last_digit
        round_a = helper_round_total(cost_a)
        round_b = helper_round_total(cost_b)
        round_c = helper_round_total(cost_c)
        return round_a + round_b + round_c 

    def is_sleeping():
        if is_hotel and is_unconscious:
            return True
        else:
            return False
    def give_rating():
        if is_michelin:
            return("5 stars")
        elif 4_star_reviews >= 50:
            return("4 stars") 