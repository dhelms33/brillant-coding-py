class Scorer:
    def __init__(self, password, attempt):
        self.password = password
        self.attempt = attempt
    
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
    
    def failed_login(self.password, self.attempt):
        failed_login_attempts = 0
        try:
            if self.password == self.attempt:
                return("Successful login!")
            elif self.password != self.attempt:
                failed_login_attempts += 1
                return("Unsuccessful login")
        except ValueError:
            return("Please enter an acceptable password")
        
    def login_success(self.password, self.attempt):
        login_success = False
        if self.password == self.attempt:
            return("Login successful")
        
    def best_password(self.password):
        best_password = False
        new_password = ""
        for char in range(len(self.password)-2):
            new_password += self.password[char] + self.password[char+1] + self.password[char-2]
        return new_password
    
    def warning(self.password, self.attempt):
        failed_attempts = 0
        while failed_attempts <= 10:
            if self.password != self.attempt:
                failed_attempts += 1
                if failed_attempts > 5:
                    return("Warning", failed_attempts, "greater than 5!")
                return failed_attempts
            elif self.attempt == self.password:
                return login_successs()
        return failed_attempts