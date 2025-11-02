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