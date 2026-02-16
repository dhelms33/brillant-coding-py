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