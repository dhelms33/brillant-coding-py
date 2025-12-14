class Scorer:
    def __init__(self, password):
        self.password = password
    
    def generate_score(self.password):
        score = 0
        uppercase = False
        if len(self.password) > 5:
            score = 5
        elif len(self.password) < 5:
            score = len(self.password)
        if self.password.isupper():
            uppercase = True
            score *= 2
        return score
    def calc_score_given_change(self.password, new_password):
        score = 0
        if len(self.password) != len(new_password):
            if len(self.password) <= len(new_password):
                score -= len(self.password)
        return score
    