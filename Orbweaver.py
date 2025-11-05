from xmlrpc.client import boolean


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
    #google what is a higher order function
    def higher_order_weaver(func, x, y):
        """ A higher order function that performs the functions of an orbweaver"""
        return func(x,y)
    def catch(prey, caught):
        caught = random(boolean)
        return(f"Caught " + {prey} + "successfully")
    
    def spiders_vs_hawks(hawks:int, spiders:int)->int:
        try:
            if hawks == 0:
                return spiders
            elif hawks == 1:
                return spiders
            elif hawks > 1: 
                spiders = hawks-1
                return spiders
            else:
                spiders = hawks-2
                return spiders
        except ValueError as e:
            return("Please enter a positive number")
        finally:
            return("The spiders will rise again.")