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
    