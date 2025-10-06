class Orbweavers:

    def __init__(self, web, length, prey):
        self.web= web
        self.length = length
        self.prey = prey
        
    def get_prey(self):
        
        return self.prey
    
    def discern_daily_cal(self):
        prey_daily = [True, False, True False]
        eat_daily = [True, True, False, True]
        prey_implies_eat = False
        for prey, eat in zip(prey_daily, eat_daily):
            if prey_daily and eat_daily:
                prey_implies_eat = True
        return prey_implies_eat