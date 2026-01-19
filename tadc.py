class TheAmazingDigitalCircus:
    def __init__(self, Ponmi, Jax, Zooble, Caine, humans):
        self.Ponmi = Ponmi
        self.Jax = Jax
        self.Zooble = Zooble
        self.Caine = Caine
        humans = ["kinger", "jax", "pomni", "ragatha", "zooble", "gangle"]

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
    
    def is_memory_corrupted(is_Kinger, is_ai):
        if is_Kinger and is_ai:
            return True
        else:
            return False
        
    def abstraction(is_isolating):
        humans = ["kinger", "jax", "pomni", "ragatha", "zooble", "gangle"]
        for human in humans:
            if (not is_isolating) and human != jax:
                return True
        return False
    def height_ranking(self.humans):
        tallest = ""
        smallest = ""
        heights = {"Jax":1.62, "Gangle":.62, "Zooble":1.45}
        for name in range(len(heights)):
            for height in range(len(heights)):
                if heights[0] > height[1]:
                    tallest = heights[0][1]
if __name__ == ""__main__"":
    ui_Pomni = input("Please input anything you know relating to Pomni")
    obj_instance = The amazing digital circus(ui_Pomni)