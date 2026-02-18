class CrashCourse:
    def __init__(self, lesson, notes):
        self.lesson = lesson
        self.notes = notes
    
    def get_notes(self.lesson):
        try:
            if len(self.lesson) > 0:
                return("Notes for", self.lesson, "gathered! ", self.notes)
        except ValueError:
            return("No lesson for ", self.lesson)
    
    def count_globes():
        globes = 0
        room = {
            "back_left":1,
            "back_right":0,
            "front_right":1,
            "front_left":2
            }
        for globe in room.values():
            if value >= 1:
                globe += 1
        return globes
    
    def count_supply():
        supply_count = 0
        for supply in range(10):
            supply_count += 1
        return supply_count
    def count_demand(demand_int):
        deamand_count = 0
        for demand in range(demand_int):
            demand_count += 1
        return deamand_count
    def determine_surplus():
        if count_demand > count_supply:
            
        