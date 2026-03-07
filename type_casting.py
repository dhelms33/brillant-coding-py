class Caster:

    def __init__(self, score):
        self.score = score
    def  calc_score(): 
        new_score = input("Enter a new score")
        avg_score = (94 + 91 + 83.5 + int(new_score)) / 4
        return("My average score is " +str(avg_score))
    
    def calc_shortest_name(name1, name2):
        min_name = min(len(name1), len(name2))
        return min_name
    def calc_abs_squared(num):
        try:
            squared = abs(num)**2
            return squared
        except ValueError as {e}:
            return("{e} is an invalid number, please try again!")
