class Reveal:
    def __init__(self):
        pass
    #TODO: Implement constructor
    def countdown_bad_bunny(duration):
        countdown = 0
        past_halfwy = False
        for second in range(duration):
            countdown = duration - second
            past_halfway = countdown >= duration/2
        return("countdown " + countdown + "past halfway? "+ past_halfway)
    
    def turn_into_dragon(number_of_wings, legs):
        try:
            if min(number_of_wings, legs) != 2:
                number_of_wings = 2
                legs = 4
                return("Dragons here have ", number_of_wings, " and ", legs ,"here")
        except ValueError as {e}:
            return("We did not understand that, please try again.")
        
    