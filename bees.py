class bees:
    def __init__(self, name, species, weather):
        self.name = name
        self.species = species
        self.weather = weather 
    def bees_when(self, weather):
        if weather == "Sunny":
            return 7
        else:
            return 1
if __name__ == "__main__":
    ui_weather = input("What's the weather? Decide it for the next seven days")
    daily_weather = ["Sunny", "rainy"]
    for weather in daily_weather: 
        bees_y_n = bees(self)
        daily_bees = bees_y_n.bees_when(ui_weather)
        results = print(daily_bees)
    