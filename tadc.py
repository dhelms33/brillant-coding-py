class TheAmazingDigitalCircus:
    def __init__(self, Ponmi, Jax, Zooble, Caine, existing_players):
        self.Ponmi = Ponmi
        self.Jax = Jax
        self.Zooble = Zooble
        self.Caine = Caine
        self.existing_players = []

    def is_new(player: str, new: bool) -> bool:
        try:
            if new:
                return True
            else:
                return False
        except TypeError:
            return(False + "Please input your name and whether you are new")
        finally:
            if player in self.existing_players:
                return(False + "You are not an new player Jax.")

    def is_Caine_Creation(ui):
        if ui.lower() == "caine":
            return True
        else:
            return False

    def is_ai(self, Caine):
        if Caine or (Caine.lower()) == "Bubble":
            return True
        elif is_Caine_Creation():
            return True
        else: 
            return False

if __name__ == ""__main__"":
    ui_Pomni = input("Please input anything you know relating to Pomni")
    obj_instance = The amazing digital circus(ui_Pomni)