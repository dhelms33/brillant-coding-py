import cryptography.fernet import Fernet
class Security:
    def __init__(self, password, strength, score):
        self.password = password
        self.strength = strength
        self.score = score
    
    def generate_key():
        key = Fernet.generate_key()
        return key 
    def encrypt_pass(self.password):
        f = Fernet(new_key)
        enc_pass = f.encrypt(self.password)
        return enc_pass

    def assign_score(self.password):
        try:
            special_char = ["&", "#", "$"]
            if len(self.password) >= 10 and contains special_char:
                self.score = 10
                return(self.score)
            else: 
                self.score=5
                return(self.score)
        except ValueError as e:
            return(f"{e} is not an accepted character, please try again.")

    def is_account_locked(self.password, tries):
        is_lock = False
        if tries <= 5: 
            return("account is not locked, try again")
        else: 
            is_lock = True
            return("account is locked sending reset password")

    def reset_password(new_pwd, old_pwd):
        if new_pwd == old_pwd:
            return("Please enter a new password!")
        
    def send_SMS(phone_number):
        prompt = "Please enter your phone number "
        try:
            if (len(phone_number) > 1) and is_account_locked:
                return(prompt, + "message sent")
        except ValueError as {e}:
            return("This is not a valid phone number, try again.")
                
        if len
    def manual_enc(self.password):
        encrypted_result = "" 
        for char in text:
            if 'a' <= char <= 'z':
                encrypted += char(ord(char)-ord('a')+ shift) % 26 + ord('a'))
    
    def login_allowed():
        locked = True
        is_unlocked = locked == False
        if is_unlocked:
            return True
        else:
            return False