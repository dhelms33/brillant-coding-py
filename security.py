class Security:
    def__init__(self, password, strength, score):
        self.password = password
        self.strength = strength
        self.score = score

    def assign_score(self.password):
        try:
            special_char = ["&", "#", "$"]
            if len(self.password) >= 10 and contains special_char:
                             self.score = 10
                return(self.score)
             else: 
                  self.score=5
        except ValueError as e:
            return(f"{e} is not an accepted character, please try again."

    def is_account_locked(self.password, tries):
        is_lock = False
        if tries <= 5: 
            return("account is not locked, try again")
        else: 
            is_lock = True
            return("account is locked sending reset password)

    def reset_password(new_pwd, old_pwd):
        if new_pwd == old_pwd:
            return("Please enter a new password!")