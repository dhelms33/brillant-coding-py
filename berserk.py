from sqlalchemy import Null


class Berserk:
    
    def __init__(self, Guts, Casca, Griffith, Skull_knight):
        self.Guts = Guts
        self.is_Guts = False
        self.Casca = Casca
        self.Griffith = Griffith
        self.Skull_knight = Skull_knight
    
    def is_Berserk(self, is_Guts, Guts):
        if is_Guts and Guts:
            return True 
        else:
            return False
    def is_griffith(self, Griffith):
        try:
            if Griffith == Null or "No":
                return("Guts smiling")
            else:
                return("GRIFFITHHHHHH!!!")
        except NameError:
            return("What you entered is not defined")
        finally:
            return("Berserk mode: active")
        
if __name__ == "__main__":
    user_input = input("Please choose an element of the manga Berserk:")
    Berserk_instance = Berserk
    result = Berserk_instance.is_Berserk(user_input)
    print(result)
    
    