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
    
    def failed_login(self.password, attempt):
        failed_login_attempts = 0
        try:
            if self.password == attempt:
                return("Successful login!")
            elif self.password != attempt:
                failed_login_attempts += 1
                return("Unsuccessful login")
        except ValueError:
            return("Please enter an acceptable password")
    
def is_strong(self.password):
    strong = False
    if len(self.password) > 8:
        strong = True
        return strong
    else:
        strong = False
        return strong
    def is_complexity(self.password):
        complexity = False
        if '#' in self.password:
            complexity = True
        return complexity